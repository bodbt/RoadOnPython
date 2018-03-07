import pymysql

try:
    conn = pymysql.connect('127.0.0.1', 'root', 'root', 'testdb')
    with conn.cursor() as cursor:
        cursor.execute("select version()")
        data = cursor.fetchone()
        print("MySQL Databese version: %s" % data)

        # create table
        cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
        sql = """CREATE TABLE EMPLOYEE (
            FIRST_NAME  CHAR(20) NOT NULL,
            LAST_NAME  CHAR(20),
            AGE INT,
            SEX CHAR(1),
            INCOME FLOAT)"""
        cursor.execute(sql)

        # insert
        sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
            LAST_NAME, AGE, SEX, INCOME)
            VALUES ('Mac', 'Mohan', 20, 'F', 2000)"""
        cursor.execute(sql)
        conn.commit()

        sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
            LAST_NAME, AGE, SEX, INCOME) \
            VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
            ('Jordan', 'Michelle', 25, 'M', 1500)
        cursor.execute(sql)
        conn.commit()

        # select
        sql = "SELECT * FROM EMPLOYEE \
            WHERE INCOME > '%d'" % (1000)
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            fname = row[0]
            lname = row[1]
            age = row[2]
            sex = row[3]
            income = row[4]
            print ("fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
                (fname, lname, age, sex, income ))

        # update
        sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
        cursor.execute(sql)
        conn.commit()

        # delete
        sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (25)
        cursor.execute(sql)
        conn.commit()
except pymysql.Error as e:
    print(e)
    print('Failed to operate mysql database.')
    conn.rollback()
finally:
    if conn:
        conn.close()
