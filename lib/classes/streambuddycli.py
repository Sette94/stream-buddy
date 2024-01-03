from buddy import Buddy
from genre import Genre


def main():
    while True:
        main_menu()
        choice = input("> ")
        if choice == "0":
            # Code to exit the CLI
            Buddy.exit_program()
        elif choice == "1":

            # Type in a streaming service, init Buddy with the service
            streamingchoice = input("Please add streaming service: ")
            buddy_instance = Buddy(streaming_service=streamingchoice)

            # User can select if they would like to search by Moive or Tv
            tv_movie()
            tv_or_movie = input("Movie(1) or Tv(2): ")

            # Movie logic and table
            if tv_or_movie == "1":
                print("All paramters are optional, click enter to skip")
                print("Avaliable Movie Genre")
                # Use the genre_options config to get all genre for movies
                # Print the genres in rows of 6
                count = 0
                for key, value in buddy_instance.genre_options(tv_or_movie).items():
                    print(f'{key:<15}', end='')  # Adjust the width as needed
                    count += 1
                    if count == 6:
                        print()
                        count = 0
                print()

                # Each input() for genre, year, actor
                genre_choice = input("Add a Genre: ")
                year_choice = input("Which Year: ")
                actor_choice = input("Add an Actor: ")

                # Call movies_in_streaming to return a json object of movies
                movies_data = buddy_instance.movies_in_streaming(
                    genre_name=genre_choice, year=year_choice, actor_name=actor_choice)

                # Call dispaly_table_movies to use the Rich package for command line tables
                buddy_instance.display_table_movies(movies_data)

            elif tv_or_movie == "2":

                print("All paramters are optional, click enter to skip")
                print("Avaliable Tv Genre")
                # Use the genre_options config to get all genre for tv(differ from movies)
                # Print the genres in rows of 6
                count = 0
                for key, value in buddy_instance.genre_options(tv_or_movie).items():
                    print(f'{key:<15}', end='')  # Adjust the width as needed
                    count += 1
                    if count == 6:
                        print()
                        count = 0
                print()

                # Each input() for genre, year
                genre_choice = input("Genre: ")
                year_choice = input("Year: ")

                # Call movies_in_streaming to return a json object of tv shows
                tv_data = buddy_instance.tv_in_streaming(
                    year=year_choice, genre_name=genre_choice
                )
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
    print("0. Exit the program")
    print("1. Use StreamBuddy")
    print("2. DB Work")


def tv_movie():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Movies")
    print("2. Tv")


if __name__ == "__main__":
    main()
