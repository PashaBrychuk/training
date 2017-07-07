
import sqlite3
import time
import hashlib

from random import randint
import random
import string
#print sqlite3.version
#print sqlite3.sqlite_version


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
        cur.execute("CREATE TABLE tags(tag_uid  TEXT, app_id  INT, state INT, ttime TEXT)")
        for i in range(random_number_of_adds()):
            print i
            a = genrandom_varchar()
            b = genrandom_int()
            c = genrandom_state()
            d = genrandom_ttime()
            print "printing a----------------------------"
            print a
            print "printing b----------------------------"
            print b
            print "printing c----------------------------"
            print c
            print "printing d----------------------------"
            print d
            sql_q = 'INSERT INTO tags VALUES({0}, {1}, {2}, {3})'.format(genrandom_varchar(), genrandom_int(), genrandom_state(), genrandom_ttime())
            cur.execute(sql_q)
            #cur.execute("INSERT INTO tags VALUES('pASJA', 12, 13, 'DSADS')")
            #cur.execute("INSERT INTO tags(tag_uid, app_id, state, ttime)  VALUES ('pasha', 2, 3, 'yura')")#cur.execute("INSERT INTO tags VALUES(genrandom_varchar(), genrandom_int(), genrandom_state(), genrandom_ttime())")


            #cur.execute("INSERT INTO tags VALUES(genrandom_varchar(), genrandom_int(), genrandom_state(), genrandom_ttime())")
        


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



def drop_db(conn):
    cur = conn.cursor()
    cur.executescript('drop table if exists tags;')

def delete_records(conn):
     pass

def select_all_data(conn):

    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tags")
 
    rows = cur.fetchall()
    #print type(rows)
 
    """for row in rows:
                    print row"""

    if len(rows)<1:
        print "Database is empty"
    else:
        print rows
 

def genrandom_varchar():
    N=21
    s = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))
    return s




def genrandom_int():
    return (randint(0, 10000))



def genrandom_state():
    return (randint(0, 2))



def genrandom_ttime():
    N=20
    s = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))
    return s


def random_number_of_adds():
    
    return (randint(0, 10))


def main():
    database = "/home/pavlobrychuk/exl"
 
    # create a database connection
    conn = create_connection(database)
    print type(conn)
    with conn:
       
      
       
        
        print "Dropping data base"
        drop_db(conn)
        
        print "Adding new data"
        add_data(conn)
        
        #print "Quering list of tables"
        #show_tables(conn)
        
        print "Selecting all data"
        select_all_data(conn)
        
        #print "Deleting all data"
        #delete_records(conn)
        
        #print "Selecting all data"
        #select_all_data(conn)
 
 
if __name__ == '__main__':
    for i in range(1,2):
        main()
        print i
        print "-"*50
        time.sleep(10)
        if i==10:
            print "The end"
        