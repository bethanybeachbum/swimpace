import psycopg2

try:
   connection = psycopg2.connect(user = "allenmarkbrown",
                                  password = "Iaabbb4life",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "python_db")
   cursor = connection.cursor()

   postgres_insert_query = """ INSERT INTO lapdata (ID, LAP_NUMBER, LAP_TIME, LAP_DATE) VALUES (%s, %s,%s, %s, )"""
   record_to_insert = (1, 1, 60.9 , "1999-01-08 04:05:06")
    #, "backstroke", "fly", "breaststroke", "kickboard", "freestyle_w_float" ,"backstroke_w_float")
   cursor.execute(postgres_insert_query, record_to_insert)

   connection.commit()
   count = cursor.rowcount
   print (count, "Record inserted successfully into lapdata table")

except (Exception, psycopg2.Error) as error :
    if(connection):
        print("Failed to insert record into lapdata table:  ", error)

finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")



## cursor.fetchall() to fetch all rows.
## cursor.fetchone() to fetch single row.
## cursor.fetchmany(SIZE) to fetch limited rows