from connection import CONN, CURSOR


class User:
    def __init__(self, first_name: str, last_name: str, age: int, user_name: str, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.user_name = user_name
        self.id = id

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, name: str):
        if isinstance(name, str) and len(name) > 0:
            self._first_name = name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, name: str):
        if isinstance(name, str) and len(name) > 0:
            self._last_name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, num: int):
        if isinstance(num, int) and num > 0:
            self._age = num

    # Setting property for username
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, name: str):
        if isinstance(name, str) and len(name) > 0 and not hasattr(self, "user_name"):
            self._user_name = name

    # creating table

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS users
            (
                id INTEGER PRIMARY KEY,
                first_name TEXT,
                last_name TEXT,
                age INTEGER,
                user_name TEXT
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

    # creating instance of the user class
    @classmethod
    def user_instance(cls, row):
        user = cls(
            id=row[0],
            first_name=row[1],
            last_name=row[2],
            age=row[3],
            user_name=row[4]
        )
        return user

    def user_data(self):
        sql = """
            INSERT INTO users(first_name, last_name, age,user_name)
            VALUES(?, ?, ?,?);
        """
        CURSOR.execute(sql, (self.first_name, self.last_name,
                       self.age, self.user_name))
        CONN.commit()

    # get all rows aka instances
    # need class methos because I am working with the whole class
    @classmethod
    def get_all(cls):
        sql = """ 
           SELECT * FROM users;
           """
        rows = CURSOR.execute(sql).fetchall()
        # turn list into list of instances
        return [cls.user_instance(row) for row in rows]

    # getting instance aka row by id
    # need class method because I am working with the whole class

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

    # Pass in user_name and return id

    def find_userid_by_user_name(cls, user_name):
        sql = """ 
            SELECT id FROM users WHERE user_name=?;
        """
        row = CURSOR.execute(sql, (user_name, )).fetchone()
        if not row:
            return None
        else:
            return cls.user_instance(row)

    # deleting instance aka row by id
    # again need class because I am working with the whole class

    @classmethod
    def delete_by_id(cls, id):
        sql = """ 
        DELETE FROM users WHERE id=?;
        """
        CURSOR.execute(sql, (id, ))
        CONN.commit()


if __name__ == "__main__":
    User.drop_table()
    User.create_table()

    # Create an instance of the User class and add data to the users table
    user_instance = User(
        first_name='Gabe', last_name='Wortmann', age=18, user_name='GabetheGreat')
    user_instance.user_data()

    user_instance = User(first_name='Dorahely',
                         last_name='Sanchez', age=27, user_name='DorahelyS')
    user_instance.user_data()

    user_instance = User(first_name='Nick', last_name='Sette',
                         age=29, user_name='Sette94')
    user_instance.user_data()

    # it works!
    # Testing get_all
    # all_users = User.get_all()

    # if all_users:
    # for user in all_users:
    # print(f"User instance: {user.__dict__}")
    # else:
    # print("No users found.")

    # it works!
    # Testing get_by_id
    # retrieved_user = User.find_user_by_id(2)
    # if retrieved_user:
    # print(f"User with id 2: {retrieved_user.__dict__}")
    # else:
    # print("User not found.")

    # Testing delete_by_id
    # Print all instances before deletion - run this to see list before deleting one
    # print("Before Deletion:")
    # for user in User.get_all():
    # print(f"ID: {user.id}, User First Name: {user.first_name}, User Last Name: {user.last_name}")

    # It works!
    # Choosing the ID I want to delete
    # user_id_to_delete = 2

    # Delete the instance with the specified ID
    # User.delete_by_id(user_id_to_delete)

    # Print all instances after deletion
    # print("\nAfter Deletion:")
    # for user in User.get_all():
    # print(f"ID: {user.id}, User First Name: {user.first_name}, User Last Name: {user.last_name}")
