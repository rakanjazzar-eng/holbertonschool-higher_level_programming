#!/usr/bin/python3
"""Lists all cities of a given state from the database hbtn_0e_4_usa."""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities "
                "JOIN states ON cities.state_id = states.id "
                "WHERE BINARY states.name = %s "
                "ORDER BY cities.id ASC", (sys.argv[4],))
    print(", ".join(row[0] for row in cur.fetchall()))
    cur.close()
    db.close()
