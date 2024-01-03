from connection import CONN, CURSOR

#from user import User


class Favorite:
    def __init__(self, movie_name, rating, user_id=None, id=None):
        self.movie_name = movie_name
        self.rating = rating
        self.user_id = user_id
        self.id = id

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
        if not row:
            return None
        else:
            return cls.favorite_instance(row)

    #deleting instance aka row by id
    #again need class because I am working with the whole class
    def delete_by_id(cls,id):
        sql = """ 
        DELETE FROM favorites WHERE id=?;
        """
        CURSOR.execute(sql, (id, ))
        CONN.commit()

'''
    def add_user(self, user):
        try:
            sql = """ 
                UPDATE favorites SET user_id=? WHERE id=?;
            """
            CURSOR.execute(sql, (user.id, self.id))
            CONN.commit()
            self.user_id = user.id
        except Exception as e:
            print(f'Something went wrong: {e}')
'''

#for testing
if __name__ == "__main__":
    
    #Favorite.create_table()
    #Favorite.drop_table()


    #add data to the favorites table
    #favorite_instance = Favorite(movie_name='Movie1', rating=5)
    #favorite_instance.saving_favorite_data()

    #favorite_instance = Favorite(movie_name='Movie2', rating=2)
    #favorite_instance.saving_favorite_data()

    #favorite_instance = Favorite(movie_name='Movie3', rating=1)
    #favorite_instance.saving_favorite_data()

    #it works!
    # Testing get_all
    #all_favorites = Favorite.get_all()

    #if all_favorites:
        #for favorite in all_favorites:
            #print(f"Favorite instance: {favorite.__dict__}")
    #else:
        #print("No favorites found.")

    # it works!
    # Testing get_by_id
    #retrieved_favorite = Favorite.find_favorite_by_id(3)
    #if retrieved_favorite:
        #print(f"Favorite with id 3: {retrieved_favorite.__dict__}")
    #else:
        #print("Favorite not found.")

    # Testing delete_by_id
    favorite_id_to_delete = 3
    Favorite.delete_by_id(favorite_id_to_delete)

    # Print remaining favorites
    remaining_favorites = Favorite.get_all()
    
    if remaining_favorites:
        for favorite in remaining_favorites:
            print(f"Favorite instance: {favorite.__dict__}")
    else:
        print("No favorites found.")
    

