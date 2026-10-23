#!/usr/bin/python3
"""Displays all values in the states table of hbtn_0e_0_usa
where name matches the argument, safe from MySQL injection."""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name = %s "
                "ORDER BY states.id ASC", (sys.argv[4],))
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
