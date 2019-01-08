#!/usr/bin/env python3

import psycopg2
import bleach
import string

DBNAME = "news"

db = psycopg2.connect(database=DBNAME)
c = db.cursor()

# FUNCTIONS
# SWITCH CASE for months


def switch(argument):
    switcher = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
    }
    return switcher.get(argument, "Invalid Month")

# PRINT QUERY RETURNS


def queryPrint(cursor):
    cursor = c.fetchall()
    cursor = ''.join(str(d) for d in cursor)
    cursor = bleach.clean(cursor)
    print("queryResponse: ", cursor)

# SPAM QUERY


def querySpam():
    # cursor.execute("UPDATE table_name SET update_column_name=(%s) WHERE ref_column_id_value = (%s)", ("column_name","value_you_want_to_update",));
    data = ("chewbbaca%", )
    query = "select path from log where path like (%s);"
    queryResponse = c.execute(query, data)
    queryPrint(queryResponse)

# SPAM UPDATE


def spamUpdate():
    query = "update log set path=(%s) where path like (%s)"
    c.execute(query,  ("chewbbaca", "spam%"))
    db.commit()

# SPAM DELETE


def spamDelete():
    data = ("chewbbaca%", )
    queryDelete = "delete from log where path like (%s)"
    c.execute(queryDelete, data)
    db.commit()

# QUERY ALL


def queryAll():
    queryResponse = c.execute("select path from log;")
    queryPrint(queryResponse)

# TASKS


def task1():
    queryResponse = c.execute("select * from pop_articles;")
    queryResponse = c.fetchall()
    print("  --//--  ")
    print("The most popular three articles: ")
    for i in range(0, len(queryResponse), 1):
        print(queryResponse[i][0] + " - " +
              str(queryResponse[i][1]) + " views")


def task2():
    queryResponse = c.execute("select * from pop_authors;")
    queryResponse = c.fetchall()
    print("  --//--  ")
    print("The most popular authors: ")
    for i in range(0, len(queryResponse), 1):
        print(queryResponse[i][0] + " - " +
              str(queryResponse[i][1]) + " views")


def task3():
    queryResponse = c.execute("select * from error_days;")
    queryResponse = c.fetchall()
    print("  --//--  ")
    print("Days with more than 1% requests leading to errors: ")
    percent = []
    for i in range(0, len(queryResponse), 1):
        percent.append('%.2f' % queryResponse[i][3])
    for i in range(0, len(queryResponse), 1):
        print(switch(queryResponse[i][0]) + " " + str(int(queryResponse[i][1])) +
              ", " + str(int(queryResponse[i][2])) + " - " + str(percent[i]) + "% errors")


# MAIN
task1()
task2()
task3()

# Close connection
db.close()
