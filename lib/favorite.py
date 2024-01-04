from connection import CONN, CURSOR

class Favorite:
    def __init__(self, movie_name: str, rating: int, user_id=None, id=None):
        self.movie_name = movie_name
        self.rating = rating
        self.user_id = user_id
        self.id = id
    
    @property
    def movie_name(self):
        return self.movie_name
    
    @movie_name.setter
    def movie_name(self, name: str):
        if isinstance(name, str) and len(name) > 0:
            self.movie_name = name
    
    @property
    def rating(self):
        return self.rating
    
    @rating.setter
    def rating(self, num: int):
        if isinstance(num, int) and num > 0:
            self.rating = num


    #creating table
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS favorites
            (
                id INTEGER PRIMARY KEY,
                movie_name TEXT,
                rating INTEGER,
                user_id INTEGER,
                FOREIGN KEY(user_id) REFERENCES users(id)
            );
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE favorites
        """
        CURSOR.execute(sql)
        CONN.commit()

    #creating instance of the favorite class
    @classmethod 
    def favorite_instance(cls, row):
        favorite = cls(
            id=row[0],
            movie_name=row[1],
            rating=row[2],
            user_id=row[3]
        )
        return favorite 

    #saving the values to each instance which means I do not use a classmethod
    def saving_favorite_data(self):
        sql = """
            INSERT INTO favorites(movie_name, rating, user_id)
            VALUES(?, ?, ?);
        """
        CURSOR.execute(sql, (self.movie_name, self.rating, self.user_id))
        CONN.commit()
        self.id = CURSOR.lastrowid
    
    #get all rows aka instances
    ##need class methos because I am working with the whole class
    @classmethod
    def get_all(cls):
           sql = """ 
           SELECT * FROM favorites;
           """
           rows = CURSOR.execute(sql).fetchall() 
           #DON'T NEED CONN.COMMT() BECAUSE NOTHIG IS BEING UPDATED JUST READING DATA
           #turn list into list of instances 
           return [cls.favorite_instance(row) for row in rows]


    #getting instance aka row by id
    #need class method because I am working with the whole class
    @classmethod
    def find_favorite_by_id(cls, id):
        sql = """ 
            SELECT * FROM favorites WHERE id=?;
        """
        row = CURSOR.execute(sql, (id, )).fetchone() 
        #DON'T NEED CONN.COMMT() BECAUSE NOTHIG IS BEING UPDATED JUST READING DATA
        if not row:
            return None
        else:
            return cls.favorite_instance(row)

    #deleting instance aka row by id
    #again need class because I am working with the whole class
    #but note can also work with an instance
    @classmethod
    def delete_by_id(cls, id):
        sql = """ 
        DELETE FROM favorites WHERE id=?;
        """
        CURSOR.execute(sql, (id, ))
        CONN.commit()

    #this is an instance method because it is going to operate on a single instance not the whole table
    def add_user(self, user_id):
        try:
        # Check if the user with the specified ID exists
            user_exists_sql = """
                SELECT id FROM users WHERE id=?;
            """
            user_exists = CURSOR.execute(user_exists_sql, (user_id,)).fetchone()

            if user_exists:
            # If user exists, update the favorite
                update_sql = """ 
                    UPDATE favorites SET user_id=? WHERE id=?;
                """
                CURSOR.execute(update_sql, (user_id, self.id))
                CONN.commit()
                self.user_id = user_id
                print(f"User with ID {user_id} associated with Favorite with ID {self.id} successfully.")
            else:
                print(f"User with ID {user_id} does not exist. No update performed.")
        except Exception as e:
            print(f'Something went wrong: {e}')


        
#for testing
if __name__ == "__main__":
    
    #Favorite.create_table()
    #Favorite.drop_table()


    #add data to the favorites table
    #favorite_instance = Favorite(movie_name='AAA', rating=5)
    #favorite_instance.saving_favorite_data()

    #favorite_instance = Favorite(movie_name='BBB', rating=2)
    #favorite_instance.saving_favorite_data()

    #favorite_instance = Favorite(movie_name='CCC', rating=1)
    #favorite_instance.saving_favorite_data()

    #it works!
    #Testing get_all
    #all_favorites = Favorite.get_all()

    #if all_favorites:
        #for favorite in all_favorites:
            #print(f"Favorite instance: {favorite.__dict__}")
    #else:
        #print("No favorites found.")

    # it works!
    # Testing get_by_id
    #retrieved_favorite = Favorite.find_favorite_by_id(2)
    #if retrieved_favorite:
        #print(f"Favorite with id 3: {retrieved_favorite.__dict__}")
    #else:
        #print("Favorite not found.")

    # Testing delete_by_id
    # Print all instances before deletion - run this to see list before deleting one
    #print("Before Deletion:")
    #for favorite in Favorite.get_all():
        #print(f"ID: {favorite.id}, Movie Name: {favorite.movie_name}, Rating: {favorite.rating}")
    
    # It works!
    # Choosing the ID I want to delete
    #favorite_id_to_delete = 2

    # Delete the instance with the specified ID
    #Favorite.delete_by_id(favorite_id_to_delete)

    # Print all instances after deletion
    #print("\nAfter Deletion:")
    #for favorite in Favorite.get_all():
        #print(f"ID: {favorite.id}, Movie Name: {favorite.movie_name}, Rating: {favorite.rating}")
    

    # testing user instance passed to favorite
    # Assuming you have instances of Favorite with ID 2 and a User with ID 3
    favorite_instance = Favorite.find_favorite_by_id(3)

   # Create a user-like dictionary for testing
    user_id_for_testing = 1

    # Check if the favorite instance is found
    if favorite_instance:
        # Add the user (with ID 3) to the favorite
        favorite_instance.add_user(user_id_for_testing)
        # printing message
        print(f"User ID associated with Favorite ID 2: {favorite_instance.user_id}")
    else:
        # printing error message
        print("Favorite not found.")
