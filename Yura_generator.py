#!/usr/bin/python
# -*- coding: utf-8 -*-
from time import gmtime, strftime
import sqlite3 as lite
import sys
import random
import time

def rand_uid():
    return random.randint(1000000, 9999999)

def rand_state():
    return random.randint(0, 2)

def t_get():
    return strftime('%a, %d %b %Y %H:%M:%S', gmtime())

con = sqlite.connect("/home/pavlobrychuk/exl")
with con:
    
    cur = con.cursor()

    while (True):
        print('generate random number of tags')
        for i in range(random.randint(1,10)):
            sql_in = 'insert into tags values("TID-{0}",{1},{2},"{3}")'.format(rand_uid(), 10, rand_state(), t_get())
            print('insert ' + sql_in)
            cur.execute(sql_in)

        con.commit() 
        tsleep = random.randint(20, 100)
        print('sleep {0} secs'.format(tsleep))
        time.sleep(tsleep)

        sql_del = 'delete from tags where rowid in (select rowid from tags limit 20)'

        cur.execute(sql_del)