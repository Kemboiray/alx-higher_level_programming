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
    cur.execute("""SELECT name FROM cities
                   WHERE state_id = (SELECT id FROM states
                       WHERE name LIKE BINARY %s
                       ORDER BY id ASC)""", (argv[4],))
    query_rows = cur.fetchall()
    try:
        for row in query_rows[:-1]:
            print(row[0], end=', ')
        print(query_rows[-1][0])
    except IndexError:
        pass
    cur.close()
    conn.close()
