import psycopg2
from pyscopg2 import Error
from time import time, ctime

try:
   connection = psycopg2.connect(user = "allenmarkbrown",
                                  password = "Iaabbb4life",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "allenmarkbrown")
   cursor = connection.cursor()
   postgreSQL_select_Query = "select * from best_times"

   cursor.execute(postgreSQL_select_Query)
   print("Selecting rows from best_times table using cursor.fetchall")
   best_times_records = cursor.fetchall() 
   
   print("Print each row and it's columns values")
   for row in best_times_records:
       print("Id = ", row[0], )
       best_time_result = row[1]
       print("Date = ",(ctime(float(best_time_result))))
       print("Date = ", row[1])
       print("Time  = ", row[2], "\n")

except (Exception, psycopg2.Error) as error :
    print ("Error while fetching data from PostgreSQL", error)

finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

## cursor.fetchall() to fetch all rows.
## cursor.fetchone() to fetch single row.
## cursor.fetchmany(SIZE) to fetch limited rows        
