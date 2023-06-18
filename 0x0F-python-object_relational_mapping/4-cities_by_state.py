#!/usr/bin/python3
"""Lists all cities from a database """

if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    cur = conn.cursor()
#    cur.execute("SELECT id, name FROM cities ORDER BY id ASC")
    cur.execute("""SELECT cities.id, cities.name, states.name AS state
                   FROM cities
                   JOIN states ON cities.state_id = states.id
                   ORDER BY cities.id ASC""")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
