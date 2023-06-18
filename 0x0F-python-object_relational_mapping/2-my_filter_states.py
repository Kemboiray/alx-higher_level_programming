#!/usr/bin/python3
"""
Lists all states with a name matching a string argument in the database
also given as a command-line argument
"""

if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("""SELECT * FROM states
                 WHERE name LIKE BINARY '{}'
                 ORDER BY id ASC""".format(argv[4]))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
