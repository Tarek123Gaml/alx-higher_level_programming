#!/usr/bin/python3

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],passwd=sys.argv[2],db=sys.argv[3])
    c = db.cursor()
    c.execute("select * from `states` order by id asc")
    for i in c:
        print(i)
