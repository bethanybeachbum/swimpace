# Tutorial from PYnative.com
# connecting to PostgreSQL database

import psycopg2
# This imports the psycopg2 module in our program. 
# Using the classes and method defined psycopg2 module we can communicate with PostgreSQL.
from psycopg2 import Error
# Using the Error class of psycopg2, we can handle any database error and exception that 
# may occur while working with PostgreSQL from Python. Using this approach we can make our 
# application robust.
# This module helps us to understand the error in detail. It returns an error message and error code.

try:
    # Using the connect() method we can create a connection to a 
    # PostgreSQL database instance. This returns a PostgreSQL Connection Object.
    connection = psycopg2.connect(user = "allenmarkbrown",
                                  password = "Iaabbb4life",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "allenmarkbrown")
    
    # create a cursor object allowing execution of PostgreSQL commands through Python source code.
    cursor = connection.cursor()
    
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")
    
    # Using the cursor’s execute method we can execute a database operation 
    # or query. Execute method takes a SQL query as a parameter.
    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    
    # We can retrieve query result using cursor methods such as fetchone(), fetchmany(), fetcthall().
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")

except (Exception, psycopg2.Error) as error:
  print("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")