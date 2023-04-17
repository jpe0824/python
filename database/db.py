import psycopg2
import csv

try:
    check = True
    while check:
        username = input('Please enter your postgres username:\n')
        password = input('Please enter your postgres password:\n')
        default_host = '127.0.0.1'
        default_port = '5432'
        default_db = 'University'
        host = input('Please enter your host ip (enter for default 127.0.0.1):')
        port = input('Please enter your port (enter for default 5432):')
        db = input('Please enter your host ip (enter for default University):')

        host = host if host else default_host
        port = port if port else default_port
        db = db if db else default_db

        try:
            connection = psycopg2.connect(
                                        user = username,
                                        password = password,
                                        host = host,
                                        port = port,
                                        database = db)
            check = False
        except:
            print('Username, password or other information incorrect\n')

    print('Loading...')

    mycursor = connection.cursor()

    mycursor.execute("""
                    select students.stuId, lastName, firstName, majorDesc, grade, classId
                    FROM students
                    LEFT JOIN enroll
                    ON students.stuId = enroll.stuId
                    LEFT JOIN majors
                    ON students.majorId = majors.majorId
                    WHERE students.stuId IN
                    (
                        SELECT students.stuId
                        FROM students
                        LEFT JOIN enroll
                        ON students.stuId = enroll.stuId
                        GROUP BY students.stuId
                        HAVING count(*) > 1
                    ) and majorDesc = 'CSC'
                    """)

    studentGPA = {}
    studentDetails = {}
    for row in mycursor:
        if row[0] in studentGPA:
            studentGPA[row[0]].append(row[4])
        else:
            studentGPA[row[0]] = [row[4]]
            studentDetails[row[0]] = (row[0], row[1], row[2], 0)

    with open('./csc_students.txt', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Id", "LastName", "FirstName", "GPA"])
        for y in sorted(studentDetails.keys()):
            gpa = 0
            for grade in studentGPA[y]:
                if grade == 'A':
                    gpa += 4
                if grade == 'B':
                    gpa += 3
                if grade == 'C':
                    gpa += 2
            gpa /= len(studentGPA[y])
            if gpa > 3.5:
                gpa = float("{0:.2f}".format(gpa))
                writer.writerow([studentDetails[y][0], studentDetails[y][1], studentDetails[y][2], gpa])
    print('File saved as ./csc_students.txt')

except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)

finally:
    mycursor.close()
    connection.close()