#import sqlite3 package
import sqlite3

#creating connection to db file
CONN = sqlite3.connect('streaming.db', timeout = 10)
#access point, what allows us to use sql queries 
#connetion between our clasess and db and let's us interact with file
CURSOR = CONN.cursor()