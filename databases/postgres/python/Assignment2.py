#!/usr/bin/python3
#
# Interface for the Assignment 4
# @author  : Kiruthika Ponnan - ASUID: 1227400293

import psycopg2
import os
import sys

def getPartitionsQuery(patiton_table_name):
    return "SELECT table_name FROM information_schema.tables \
        WHERE table_name ~ '{partition_table}[0-9]$'".format(partition_table=patiton_table_name)

# Donot close the connection inside this file i.e. do not perform openconnection.close()
def RangeQuery(ratingsTableName, ratingMinValue, ratingMaxValue, openconnection):

    # Create a cursor object to execute SQL queries
    cursor = openconnection.cursor()

    # Get the list of partition tables for the given ratings table
    list_partitions_query_rr = getPartitionsQuery('roundrobinratingspart')
    cursor.execute(list_partitions_query_rr)
    partition_tables_rr = cursor.fetchall()

    # Get the list of partition tables for the given ratings table
    list_partitions_query_r = getPartitionsQuery('rangeratingspart')
    cursor.execute(list_partitions_query_r)
    partition_tables_r = cursor.fetchall()

    partition_tables = partition_tables_rr + partition_tables_r

    # Create the output file
    output_file = "RangeQueryOut.txt"
    
    # Process each partition table
    for partition_table in partition_tables:
        partition_name = partition_table[0]
        
        # Retrieve the tuples from the partition table within the rating range
        select_query = "SELECT '{partition_name}', UserID, MovieID, Rating \
            FROM {partition_name} \
            WHERE Rating >= {rating_min_value} AND Rating <= {rating_max_value} \
            ".format(partition_name=partition_name, rating_min_value=ratingMinValue, rating_max_value=ratingMaxValue)
        cursor.execute(select_query)
        rows = cursor.fetchall()

        # Write the retrieved tuples to the output file
        writeToFile(output_file, rows)
    
    # Commit the changes and close the cursor and connection
    openconnection.commit()


def PointQuery(ratingsTableName, ratingValue, openconnection):

    # Create a cursor object to execute SQL queries
    cursor = openconnection.cursor()

    # Get the list of partition tables for the given ratings table
    list_partitions_query_rr = getPartitionsQuery('roundrobinratingspart')
    cursor.execute(list_partitions_query_rr)
    partition_tables_rr = cursor.fetchall()

    # Get the list of partition tables for the given ratings table
    list_partitions_query_r = getPartitionsQuery('rangeratingspart')
    cursor.execute(list_partitions_query_r)
    partition_tables_r = cursor.fetchall()

    partition_tables = partition_tables_rr + partition_tables_r

    # Create the output file
    output_file = "PointQueryOut.txt"
    
    # Process each partition table
    for partition_table in partition_tables:
        partition_name = partition_table[0]
        
        # Retrieve the tuples from the partition table with the specified rating value
        select_query = "SELECT '{partition_name}', UserID, MovieID, Rating \
            FROM {partition_name} \
            WHERE Rating = {rating_value} \
            ".format(partition_name=partition_name, rating_value=ratingValue)
        cursor.execute(select_query)
        rows = cursor.fetchall()

        # Write the retrieved tuples to the output file
        writeToFile(output_file, rows)
        #sanitize_output_file(output_file)

    # Commit the changes and close the cursor and connection
    openconnection.commit()


def writeToFile(filename, rows):
    f = open(filename, 'a')
    for line in rows:
        f.write(','.join(str(s) for s in line))
        f.write('\n')
    f.close()
