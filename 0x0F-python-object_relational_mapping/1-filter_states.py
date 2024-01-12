#!/usr/bin/python3

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost",port=3306,user=argv[1],
            passwd=argv[2],db=argv[3],charset="utf8")

    cur = conn.cursor()

    cur.execute("select * from states order by id asc")
    for i in cur.fetchall():
        if i[1].startwith("N"):
            print(i)
