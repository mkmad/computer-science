#!/usr/bin/python3

# Interface for the assignement
# @author  : Kiruthika Ponnan - ASUID: 1227400293

import psycopg2
import os
import sys


RANGE_TABLE_PREFIX = 'rangeratingspart'
RROBIN_TABLE_PREFIX = 'roundrobinratingspart'
USER_ID_COLNAME = 'userid'
MOVIE_ID_COLNAME = 'movieid'
RATING_COLNAME = 'rating'

def getOpenConnection(user='postgres', password='1234', dbname='postgres'):
    return psycopg2.connect("dbname='" + dbname + "' user='" + user + "' host='db' password='" + password + "'")


def loadRatings(ratingstablename, ratingsfilepath, openconnection):
    
    print("Loading ratings table")
    # Create a cursor object to execute SQL queries
    cursor = openconnection.cursor()
    
    # Create the Ratings table if it doesn't exist
    create_table_query = "CREATE TABLE IF NOT EXISTS {0} \
        (UserID INT, MovieID INT, Rating FLOAT)".format(ratingstablename)
    cursor.execute(create_table_query)
    openconnection.commit()
    
    # Open the ratings.dat file
    with open(ratingsfilepath, 'r') as file:
        # Read each line in the file
        for line in file:
            # Split the line into UserID, MovieID, and Rating
            user_id, movie_id, rating, _ = line.split("::")
            
            # Insert the values into the Ratings table
            insert_query = "INSERT INTO Ratings (UserID, MovieID, Rating) \
                VALUES ({0}, {1}, {2})".format(user_id, movie_id, rating)
            cursor.execute(insert_query)
    
    # Commit the changes to the database
    openconnection.commit()



def rangePartition(ratingstablename, numberofpartitions, openconnection):
    
    # Create a cursor object to execute SQL queries
    cursor = openconnection.cursor()
    
    # Get the minimum and maximum rating values from the Ratings table
    min_query = "SELECT MIN(Rating) FROM {ratingstablename}".format(ratingstablename=ratingstablename)
    max_query = "SELECT MAX(Rating) FROM {ratingstablename}".format(ratingstablename=ratingstablename)
    cursor.execute(min_query)
    min_rating = cursor.fetchone()[0]
    cursor.execute(max_query)
    max_rating = cursor.fetchone()[0]
    
    # Calculate the range size for each partition
    range_size = (max_rating - min_rating) / numberofpartitions
    
    # Create the partition tables
    for i in range(numberofpartitions):
        partition_name = "{RANGE_TABLE_PREFIX}{num}".format(
            RANGE_TABLE_PREFIX=RANGE_TABLE_PREFIX, 
            ratingstablename=ratingstablename, num=i)
        create_partition_query = "CREATE TABLE IF NOT EXISTS {partition_name} AS \
            SELECT * FROM {ratingstablename} \
            WHERE Rating > {num} \
            AND Rating <= {num} + 1".format(
                partition_name=partition_name, 
                ratingstablename=ratingstablename, 
                min_rating=min_rating, 
                range_size=range_size,
                num=i
        )
        cursor.execute(create_partition_query)

    # Insert min_rating into the first partition
    partition_name = "{RANGE_TABLE_PREFIX}{num}".format(
        RANGE_TABLE_PREFIX=RANGE_TABLE_PREFIX, 
        ratingstablename=ratingstablename, num=0)
    create_partition_query = "INSERT INTO {partition_name} (UserID, MovieID, Rating) \
        ( SELECT * FROM {ratingstablename} \
          WHERE Rating = {num})".format(
            partition_name=partition_name, 
            ratingstablename=ratingstablename, 
            min_rating=min_rating, 
            range_size=range_size,
            num=min_rating
    )
    cursor.execute(create_partition_query)

    # Commit the changes and close the cursor and connection
    openconnection.commit()


def roundRobinPartition(ratingstablename, numberofpartitions, openconnection):

    # Create a cursor object to execute SQL queries
    cursor = openconnection.cursor()

    # Get the total number of rows in the Ratings table
    count_query = "SELECT COUNT(*) FROM {ratings_table}".format(ratings_table=ratingstablename)
    cursor.execute(count_query)
    total_rows = cursor.fetchone()[0]
    
    # Create the partition tables
    for i in range(numberofpartitions):
        partition_name = "{RROBIN_TABLE_PREFIX}{num}".format(
            RROBIN_TABLE_PREFIX=RROBIN_TABLE_PREFIX, 
            ratingstablename=ratingstablename, num=i)
        # Calculate the starting row index for the partition
        start_index = i
        
        # Generate the SQL query to create the partition table using the round-robin approach
        create_partition_query = "CREATE TABLE IF NOT EXISTS {partition_name} AS \
            SELECT * FROM ( \
                SELECT *, \
                ROW_NUMBER() OVER () AS row_number \
                FROM {ratings_table} \
            ) AS temp \
            WHERE (row_number - 1) % {num_partitions} = {start_index} \
        ".format( 
            partition_name=partition_name, 
            ratings_table=ratingstablename, 
            num_partitions=numberofpartitions, 
            start_index=start_index)
        cursor.execute(create_partition_query)
    
    # Commit the changes 
    openconnection.commit()


def roundrobininsert(ratingstablename, userid, itemid, rating, openconnection):

    # Create a cursor object to execute SQL queries
    cursor = openconnection.cursor()
    
    # Get the total number of partitions
    count_partitions_query = "SELECT COUNT(*) FROM information_schema.tables WHERE table_name LIKE 'rrobin_part%'"
    cursor.execute(count_partitions_query)
    num_partitions = cursor.fetchone()[0]
    
    total_rows_query = ""
    for i in range(num_partitions - 1):
        total_rows_query += "select count(*) from rrobin_part{0} union all ".format(i)

    total_rows_query += "select count(*) from rrobin_part{0}".format(num_partitions - 1)
    
    total_rows_query = "SELECT SUM(count) FROM ({0}) AS temp".format(total_rows_query)
    print(total_rows_query)
    cursor.execute(total_rows_query)
    total_rows = cursor.fetchone()[0]

    print(total_rows)
    # Calculate the next row number based on the round-robin approach
    next_row_number = (total_rows) % num_partitions

    partition_name = "{RROBIN_TABLE_PREFIX}{num}".format(
        RROBIN_TABLE_PREFIX=RROBIN_TABLE_PREFIX, 
        ratingstablename=ratingstablename, num=next_row_number)

    # Insert the new tuple into the appropriate partition
    insert_query = "INSERT INTO {partition_name} \
        (UserID, MovieID, Rating) \
        VALUES ({user_id}, {movie_id}, {rating})".format(
            partition_name=partition_name, 
            user_id=userid, 
            movie_id=itemid, 
            rating=rating)
    cursor.execute(insert_query)
    
    # Commit the changes 
    openconnection.commit()


def rangeinsert(ratingstablename, userid, itemid, rating, openconnection):
    # Create a cursor object to execute SQL queries
    cursor = openconnection.cursor()

    # Get partition number for the given rating
    partition = 0
    if 1 < rating <= 2:
        partition = 1
    elif 2 < rating <= 3:
        partition = 2
    elif 3 < rating <= 4:
        partition = 3
    elif 4 < rating <= 5:
        partition = 4

    # Insert the values into the Ratings table
    partition_name = "{RANGE_TABLE_PREFIX}{partition}".format(
        RANGE_TABLE_PREFIX=RANGE_TABLE_PREFIX, 
        ratingstablename=ratingstablename, partition=partition)
    
    # Insert the values into the Ratings table query
    insert_query = "INSERT INTO {0} (UserID, MovieID, Rating) \
        VALUES ({1}, {2}, {3})".format(partition_name, userid, itemid, rating)
    cursor.execute(insert_query)

    # Commit the changes and close the cursor and connection
    openconnection.commit()


def createDB(dbname='dds_assignment'):
    """
    We create a DB by connecting to the default user and database of Postgres
    The function first checks if an existing database exists for a given name, else creates it.
    :return:None
    """
    # Connect to the default database
    con = getOpenConnection(dbname='postgres')
    con.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    cur = con.cursor()

    # Check if an existing database with the same name exists
    cur.execute('SELECT COUNT(*) FROM pg_catalog.pg_database WHERE datname=\'%s\'' % (dbname,))
    count = cur.fetchone()[0]
    if count == 0:
        cur.execute('CREATE DATABASE %s' % (dbname,))  # Create the database
    else:
        print('A database named {0} already exists'.format(dbname))

    # Clean up
    cur.close()
    con.close()

def deletepartitionsandexit(openconnection):
    cur = openconnection.cursor()
    cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
    l = []
    for row in cur:
        l.append(row[0])
    for tablename in l:
        cur.execute("drop table if exists {0} CASCADE".format(tablename))

    cur.close()

def deleteTables(ratingstablename, openconnection):
    try:
        cursor = openconnection.cursor()
        if ratingstablename.upper() == 'ALL':
            cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
            tables = cursor.fetchall()
            for table_name in tables:
                cursor.execute('DROP TABLE %s CASCADE' % (table_name[0]))
        else:
            cursor.execute('DROP TABLE %s CASCADE' % (ratingstablename))
        openconnection.commit()
    except psycopg2.DatabaseError as e:
        if openconnection:
            openconnection.rollback()
        print('Error %s' % e)
    except IOError as e:
        if openconnection:
            openconnection.rollback()
        print('Error %s' % e)
    finally:
        if cursor:
            cursor.close()
