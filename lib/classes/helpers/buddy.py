import logging
from props.properties import BaseProperties
from classes.configs.streaming import Streaming
from classes.configs.genre import Genre
from classes.configs.actor import Actor
from rich.console import Console
from rich.table import Table
from rich import box
from rich.style import Style

FORMAT = '%(asctime)-15s %(filename)s - %(lineno)d - %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)
logger = logging.getLogger(__name__)


class Buddy:
    def __init__(self, streaming_service_name) -> None:
        self.base_props = BaseProperties()
        self.streaming_config = Streaming()
        self.genre_config = Genre()
        self.actor_config = Actor()
        self.streaming_service_name = streaming_service_name
        self.streaming_service_id = self.streaming_config.streaming_service_id(
            streaming_service_name)

    @property
    def streaming_service_id(self):
        return self._streaming_service_id

    @streaming_service_id.getter
    def streaming_service_id(self):
        return self._streaming_service_id

    @streaming_service_id.setter
    def streaming_service_id(self, val):
        if isinstance(val, int):
            self._streaming_service_id = val
        else:
            raise ValueError(
                f"Streaming service {self.streaming_service_name} is not valid. Here are some popular ones:\nNetflix\nHulu\nAmazon Prime Video\nParamount Plus\nApple TV Plus")

    def movies_in_streaming(self, year="", genre_name="", actor_name=""):

        movies_by_service = self.streaming_config.movies_by_streaming_service(
            self.streaming_service_id,
            year,
            self.genre_config.genre_id_movie(genre_name),
            self.actor_config.actor_id(actor_name.replace(" ", "%20")))

        return movies_by_service.get("results")

    def tv_in_streaming(self, year="", genre_name=""):

        tv_by_service = self.streaming_config.tv_by_streaming_service(
            self.streaming_service_id,
            year,
            self.genre_config.genre_id_tv(genre_name))

        return tv_by_service.get("results")

    def display_table_movies(self, movies):
        table = Table(title=self.streaming_service_name,
                      box=box.HEAVY, show_lines=True)

        title_style = Style(color="White", bold=True, underline=True)
        table.title_style = title_style

        rows = [
            [movie.get('original_title', 'N/A'), movie.get('overview', 'N/A'),
             movie.get('release_date', 'N/A'), movie.get('poster_path', 'N/A')]
            for movie in movies
        ]

        columns = ["Title", "Plot", "Release Date", "Poster"]

        for column in columns:
            table.add_column(column, justify="center", style="red")

        for row in rows:
            # Make each cell in the "Poster" column clickable with the corresponding URL
            for i, cell_value in enumerate(row):
                if columns[i] == "Poster":
                    cell_text = "https://image.tmdb.org/t/p/original" + \
                        cell_value if cell_value is not None else "No Poster Availiable"
                    row[i] = cell_text
                else:
                    row[i] = cell_value

            table.add_row(*row)

        console = Console()
        console.print(table)

    def display_table_tv(self, tvs):
        table = Table(title=self.streaming_service_name,
                      box=box.HEAVY, show_lines=True)

        title_style = Style(color="White", bold=True, underline=True)
        table.title_style = title_style

        rows = [
            [tv.get('original_name', 'N/A'), tv.get('overview', 'N/A'),
             tv.get('first_air_date', 'N/A'), tv.get('poster_path', 'N/A')]
            for tv in tvs
        ]

        columns = ["Title", "Plot", "Release Date", "Poster"]

        for column in columns:
            table.add_column(column, justify="center", style="red")

        for row in rows:
            # Make each cell in the "Poster" column clickable with the corresponding URL
            for i, cell_value in enumerate(row):
                if columns[i] == "Poster":
                    cell_text = "https://image.tmdb.org/t/p/original" + \
                        cell_value if cell_value is not None else "No Poster Availiable"
                    row[i] = cell_text
                else:
                    row[i] = cell_value

            table.add_row(*row)

        console = Console()
        console.print(table)

    def exit_program():
        print("Goodbye!")
        exit()

    def genre_options(self, type):
        if type == "1":
            return self.genre_config.movie_genre()
        else:
            return self.genre_config.tv_genre()


if __name__ == '__main__':
    buddy_instance = Buddy(streaming_service_name="Netflix")
    print(buddy_instance.streaming_service_id)

    movies_data = buddy_instance.movies_in_streaming(
        genre_name="Comedy", year="", actor_name="")
    buddy_instance.display_table_movies(movies_data)

    # tv_data = buddy_instance.tv_in_streaming(
    #     year="1999", genre_name="Action &"
    # )
    # buddy_instance.display_table_tv(tv_data)
