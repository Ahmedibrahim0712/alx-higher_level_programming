#!/usr/bin/python3
"""Lists states"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    c = db.cursor()
    c.execute("SELECT * FROM states")
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
