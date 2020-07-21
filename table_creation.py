# table creation in postgresql

import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(user = "allenmarkbrown",
                                  password = "Iaabbb4life",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "allenmarkbrown")

    cursor = connection.cursor()
    
    create_table_query = '''CREATE TABLE best_times
          (ID INT PRIMARY KEY     NOT NULL,
          DATE           TEXT    NOT NULL,
          TIME         REAL); '''
    
    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully in PostgreSQL ")

except (Exception, psycopg2.DatabaseError) as error :
    print ("Error while creating PostgreSQL table", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")