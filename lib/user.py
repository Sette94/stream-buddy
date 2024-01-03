#import CONN from 'connection.py'
#import CURSOR from 'connection.py'

from connection import CONN, CURSOR

class User:
    def __init__(self, first_name, last_name, age, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.id = id

    #creating table
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS users
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
            DROP TABLE IF EXISTS users
        """
        CURSOR.execute(sql)
        CONN.commit()
        
    def user_data(self):
        sql = """
            INSERT INTO users(first_name, last_name, age)
            VALUES(?, ?, ?);
        """
        CURSOR.execute(sql,(self.first_name, self.last_name, self.age))
        CONN.commit()


    #need to debug!!
    @classmethod
    def find_user_by_id(cls,id):
       
    
if __name__ == "__main__":
    #User.create_table()
    #User.drop_table()

    #Create an instance of the User class and add data to the users table
    #user_instance = User(first_name='John', last_name='Doe', age=25)
    #user_instance.user_data()
    #user_instance = User(first_name='Jane', last_name='Doe', age=30)
    #user_instance.user_data()
    

    #need to debug
    #grabbing user by id
    #existing_user = User.get_user_by_id(1)





