from classes.helpers.buddy import Buddy
from classes.helpers.audio_helper import Audio


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
""")

            # Type in a streaming service, init Buddy with the service
            streamingchoice = input("Please add streaming service: ")
            buddy_instance = Buddy(streaming_service_name=streamingchoice)

            Audio.play_audio(Audio.audio_convert.get((streamingchoice)))

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
            print("Empty")
        else:
            print("Invalid choice")


def main_menu():
    print("Please select an option:")
    print("1. Use StreamBuddy")
    print("2. DB Work")
    print("0. Exit the program")


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
