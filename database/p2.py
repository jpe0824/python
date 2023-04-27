import psycopg2
try:
    connection = psycopg2.connect(user="postgres",password="lakers", host="127.0.0.1",port="5432",database="fitness")
    cursor = connection.cursor()
    postgreSQL_select_Query = """
                            SELECT * FROM workout_summary;
                                """
    cursor.execute(postgreSQL_select_Query)
    rows = cursor.fetchall()
    print("Print each row and it's columns values")
    for row in rows:
        print(f"username: {row[0]}")
        print(f"date: {row[1]}")
        print(f"exercise: {row[2]}")
        print(f"minutes: {row[3]}")
        print(f"calories: {row[4]}")
except (Exception, psycopg2.Error) as error :
    print ("Error while fetching data from PostgreSQL", error)
finally:
    #closing database connection.
    cursor.close()
    connection.close()
    print("PostgreSQL connection is closed")
