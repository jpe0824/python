import psycopg2

try:
    connection = psycopg2.connect(user = 'postgres',
                                password='lakers',
                                host='127.0.0.1',
                                port='5432',
                                database='university')

    mycursor = connection.cursor()

    mycursor.execute("select students.stuId, lastName, firstName FROM students")

    for row in mycursor:
        print(row)

except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)

finally:
    mycursor.close()
    connection.close()