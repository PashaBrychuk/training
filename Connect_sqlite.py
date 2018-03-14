#Connect_sqlite.py


import sqlite3
from sqlite3 import Error

def create_connection(db_file):
	 """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
    	connection = sqlite3.connection(db_file)
    	return connection
    except Error as e:
    	print e
    return None