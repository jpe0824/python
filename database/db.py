import psycopg2
import csv

try:
    print('Loading...')
    connection = psycopg2.connect(user = 'postgres',
                                password='*********',
                                host='127.0.0.1',
                                port='5432',
                                database='University')

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
        for y in studentDetails:
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
    print('File saved as ./csc_students.csv')

except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)

finally:
    mycursor.close()
    connection.close()