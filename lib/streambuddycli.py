from classes.helpers.buddy import Buddy
from classes.helpers.audio_helper import Audio
from user import User
from favorite import Favorite


def main():
    while True:
        main_menu()
        choice = input("> ")
        if choice == "0":
            Buddy.exit_program()  # Code to exit the CLI
        elif choice == "1":

            print("""
                 _____                                ____            _     _
                / ____| |                            |  _ \          | |   | |      
               | (___ | |_ _ __ ___  __ _ _ __ ___   | |_) |_   _  __| | __| |_   _ 
                \___ \| __| '__/ _ \/ _` | '_ ` _ \  |  _ <| | | |/ _` |/ _` | | | |
                ____) | |_| | |  __/ (_| | | | | | | | |_) | |_| | (_| | (_| | |_| |
               |_____/ \__|_|  \___|\__,_|_| |_| |_| |____/ \__,_|\__,_|\__,_|\__, |
                                                                               __/ |
                                                                               |___/ 
                                   Stop Scrolling!
                """)

            # Type in a streaming service, init Buddy with the service
            streamingchoice = input("Please add streaming service: ")
            buddy_instance = Buddy(streaming_service_name=streamingchoice)

            if Audio.audio_visual_convert.get(streamingchoice):
                print(Audio.audio_visual_convert.get(streamingchoice)[1])
                Audio.play_audio(
                    Audio.audio_visual_convert.get(streamingchoice)[0])

            tv_movie()  # User can select if they would like to search by Moive or Tv
            tv_or_movie = input("Movie(1) or Tv(2): ")

            if tv_or_movie == "1":  # Movie logic and table
                print("All paramters are optional, click enter to skip")
                print("Avaliable Movie Genre")

                count = 0
                # Use the genre_options config to get all genre for movies, print the genres in rows of 6
                for key, value in buddy_instance.genre_options(tv_or_movie).items():
                    print(f'{key:<15}', end='')  # Adjust the width as needed
                    count += 1
                    if count == 6:
                        print()
                        count = 0
                print()

                genre_choice = get_valid_genre_choice(
                    buddy_instance, tv_or_movie)  # Input for Genre, will only return if valid genre or is skipped
                year_choice = input("Which Year: ")  # Input for Year
                actor_choice = input("Add an Actor: ")  # Input for Actor

                movies_data = buddy_instance.movies_in_streaming(
                    genre_name=genre_choice, year=year_choice, actor_name=actor_choice)  # Call movies_in_streaming to return a json object of movies

                # Call dispaly_table_movies to use the Rich package for command line tables
                buddy_instance.display_table_movies(movies_data)

            elif tv_or_movie == "2":

                print("All paramters are optional, click enter to skip")
                print("Avaliable Tv Genre")

                count = 0
                # Use the genre_options config to get all genre for tv(differ from movies), print the genres in rows of 6
                for key, value in buddy_instance.genre_options(tv_or_movie).items():
                    print(f'{key:<15}', end='')  # Adjust the width as needed
                    count += 1
                    if count == 6:
                        print()
                        count = 0
                print()

                genre_choice = get_valid_genre_choice(
                    buddy_instance, tv_or_movie)  # Input for Genre, will only return if valid genre or is skipped
                year_choice = input("Year: ")  # Input for Year

                tv_data = buddy_instance.tv_in_streaming(
                    year=year_choice, genre_name=genre_choice
                )  # Call movies_in_streaming to return a json object of tv shows

                # Call dispaly_table_tv to use the Rich package for command line tables
                buddy_instance.display_table_tv(tv_data)

            else:
                print("Returning to main menu")
                main_menu()

        elif choice == "2":

            db_menu()
            db_choice = input("> ")

            if db_choice == "1":

                user_name = input(
                    "Please sign in with username to see favorites: ")

                signed_in_user_id = [
                    user.id for user in User.get_all() if user_name == user.user_name][0]  # Id from User table of the user signed in

                set_a_favorite = input(
                    "Do you want to set a new favorite (yes,no): ")

                if set_a_favorite == "yes":
                    user_movie = input("Add a movie: ")
                    user_rating = int(input("Add a rating: "))

                    favorite_instance = Favorite(
                        movie_name=user_movie, rating=user_rating)
                    favorite_instance.saving_favorite_data()

                    # Check if the favorite instance is found
                    if favorite_instance:
                        favorite_instance.add_user(signed_in_user_id)
                    else:
                        print("Favorite not found.")

                users_favorite_movies = Favorite.find_favorite_by_userid(
                    signed_in_user_id)

                if users_favorite_movies:
                    favorites = [
                        movies.movie_name for movies in users_favorite_movies]
                    print(f"Here is a list of {user_name}'s favorite movies")
                    # Start index from 1
                    for index, value in enumerate(favorites, 1):
                        print(f"{index}. {value}")
                    print()
                else:
                    print(f"{user_name} does not have any favorites")

            elif db_choice == "2":
                new_user_first_name = input("Enter your first name: ")
                new_user_last_name = input("Enter your last name: ")
                new_user_age = int(input("Enter your age: "))
                new_user_user_name = input("Enter your username: ")

                try:
                    if User.find_userid_by_user_name(new_user_user_name):
                        print(f"Username {new_user_user_name} already exists")
                    else:
                        user_instance = User(first_name=new_user_first_name, last_name=new_user_last_name,
                                             age=new_user_age, user_name=new_user_user_name)
                        user_instance.user_data()
                        print(
                            f"Successfully created new user {new_user_user_name}")
                except Exception as e:
                    print(e)

            elif db_choice == "3":
                delete_user_name = input("Enter your username: ")

                try:
                    if User.find_userid_by_user_name(delete_user_name):
                        User.delete_by_user_name(delete_user_name)
                        print(f"Successfully deleted user {delete_user_name}")
                    else:
                        print(
                            f"There is not record of this user {delete_user_name}")

                except Exception as e:
                    print(f"Invalid username {e}")

            elif db_choice == "4":
                user_name = input("Enter your current username: ")

                update_user_name = input("Enter your new username: ")

                try:
                    User.update_by_user_name(update_user_name, user_name)
                    print(
                        f"Successfully updated username from {user_name} to {update_user_name}")
                except Exception as e:
                    print(f"Invalid username {e}")
                pass

        else:
            print("Invalid choice")


def main_menu():
    print("Please select an option:")
    print("1. Use StreamBuddy")
    print("2. View Favorites Database")
    print("0. Exit the program")


def db_menu():
    print("Please select an option:")
    print("1. Sign in with username")
    print("2. Create username")
    print("3. Delete username")
    print("4. Update username")


def tv_movie():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Movies")
    print("2. Tv")


def get_valid_genre_choice(buddy_instance, tv_or_movie):
    while True:
        genre_choice = input("Add a Genre: ")
        if genre_choice is not None and len(genre_choice) > 0:
            if buddy_instance.genre_options(tv_or_movie).get(genre_choice) is not None:
                return genre_choice
            else:
                print("Please choose a correct genre.")
        else:
            return ""


if __name__ == "__main__":
    main()
