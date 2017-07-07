#select_from_sqlite

import sqlite3
print sqlite3.version
print sqlite3.sqlite_version

from sqlite3 import Error
 
 
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect("/home/pavlobrychuk/exl")
        return conn
    except Error as e:
        print(e)
 
    return None

def add_data(conn):
    with conn:
    
        cur = conn.cursor()    
        cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
        cur.execute("INSERT INTO Cars VALUES(1,'Audi',52642)")
        cur.execute("INSERT INTO Cars VALUES(2,'Mercedes',57127)")
        cur.execute("INSERT INTO Cars VALUES(3,'Skoda',9000)")
        cur.execute("INSERT INTO Cars VALUES(4,'Volvo',29000)")
        cur.execute("INSERT INTO Cars VALUES(5,'Bentley',350000)")
        cur.execute("INSERT INTO Cars VALUES(6,'Citroen',21000)")
        cur.execute("INSERT INTO Cars VALUES(7,'Hummer',41400)")
        cur.execute("INSERT INTO Cars VALUES(8,'Volkswagen',21600)")



def show_tables(conn):
    res  = conn.execute("select name from sqlite_master where type='table'")
    s = []
    """cur = conn.cursor()
                cur.execute(".tables")
                tables = cur.fetchall()
                """
    for i in res:
        print 
        s.append(i)
    print "we have next tables", s 
    return s


def check_version(conn):
    cur = conn.cursor()
    cur.execute("select sqlite_version()")
    version = cur.fetchall()
    
        
    print "sqlite_version is", version 







def select_all_tasks(conn):

    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Cars")
 
    rows = cur.fetchall()
    print type(rows)
 
    for row in rows:
        print(row)
 
 


def main():
    database = "/home/pasha/exl "
 
    # create a database connection
    conn = create_connection(database)
    print type(conn)
    with conn:
        add_data(conn)
        print "Query all tasks"
        select_all_tasks(conn)
        print "Quering data base version"
        check_version(conn)
        #add_data(conn)
        print "Quering list of tables"
        show_tables(conn)
 
 
if __name__ == '__main__':
    main()  