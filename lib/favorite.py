from connection import CONN, CURSOR

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

    def favorite_data(self):
        sql = """
            INSERT INTO favorites(movie_name, rating, user_id)
            VALUES(?, ?, ?);
        """
        CURSOR.execute(sql,(self.movie_name, self.rating, self.user_id))
        CONN.commit()

if __name__ == "__main__":
    Favorite.create_table()
    #Favorite.drop_table()

# add data to the users table
    favorite_instance = Favorite(movie_name='Test', rating=5)
    favorite_instance.favorite_data()
