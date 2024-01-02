#import CONN from 'connection.py'
#import CURSOR from 'connection.py'

from connection import CONN, CURSOR

class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    #creating table
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE users
            (
                id INTEGER PRIMARY KEY,
                first_name TEXT,
                last_name TEXT,
                age INTEGER
            );
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE users
        """
        CURSOR.execute(sql)
        CONN.commit()
        

if __name__ == "__main__":
    User.create_table()
    #User.drop_table()





