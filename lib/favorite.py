from connection import CONN, CURSOR

class Favorite:
    def __init__(self, movie_name, rating, user_id):
        self.movie_name = movie_name
        self.rating = rating
        self.user_id = user_id

    #creating table
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE favorites
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

if __name__ == "__main__":
    Favorite.create_table()
    #Favorite.drop_table()
