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

    #creating instance of the user class
    @classmethod 
    def user_instance(cls, row):
        user = cls(
            id=row[0],
            first_name=row[1],
            last_name=row[2],
            age=row[3],
        )
        return user 
        
    def user_data(self):
        sql = """
            INSERT INTO users(first_name, last_name, age)
            VALUES(?, ?, ?);
        """
        CURSOR.execute(sql,(self.first_name, self.last_name, self.age))
        CONN.commit()
    
    #get all rows aka instances
    ##need class methos because I am working with the whole class
    @classmethod
    def get_all(cls):
           sql = """ 
           SELECT * FROM users;
           """
           rows = CURSOR.execute(sql).fetchall() 
           #turn list into list of instances 
           return [cls.user_instance(row) for row in rows]


    #getting instance aka row by id
    #need class method because I am working with the whole class
    @classmethod
    def find_user_by_id(cls, id):
        sql = """ 
            SELECT * FROM users WHERE id=?;
        """
        row = CURSOR.execute(sql, (id, )).fetchone() 
        if not row:
            return None
        else:
            return cls.user_instance(row)

    #deleting instance aka row by id
    #again need class because I am working with the whole class
    def delete_by_id(cls,id):
        sql = """ 
        DELETE FROM users WHERE id=?;
        """
        CURSOR.execute(sql, (id, ))
        CONN.commit()


    #need to debug!!
     # @classmethod
     # def find_user_by_id(cls,id):
       

#if __name__ == "__main__":
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





