#!/usr/bin/python3
""" DOCUMENTATIONS """
import MySQLdb as DB
import sys

if __name__ == "__main__":
    if len(sys.argv) == 4:
        db_username = sys.argv[1]
        db_password = sys.argv[2]
        db_name = sys.argv[3]
        conn  = DB.connect(host="localhost", port=3306,
                                user=db_username,
                                passwd=db_password,
                                db=db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM states ORDER BY states.id")
        rows_selected = cursor.fetchall()
        for row in rows_selected:
            print(row)

        cursor.close()
        conn.close()