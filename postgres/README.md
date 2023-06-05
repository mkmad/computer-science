Docker Commands

 start
 `docker run -itd -e POSTGRES_USER=postgres -e POSTGRES_HOST_AUTH_METHOD=trust -p 5432:5432 -v ~/projects/kponnan-511/data/:/var/lib/postgresql/data --name postgresql postgres:10`

 run sql script 

 <!-- Assignment 1 -->
 `cat solution1.sql | docker exec -i postgresql psql -U postgres`

 <!-- Assignment 2 (passing env var to the queries) --> 
  `cat solution2.sql | docker exec -i postgresql psql -U postgres -v v1=110`
