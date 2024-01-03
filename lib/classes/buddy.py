import logging
from properties import BaseProperties
from streaming import Streaming
from genre import Genre
from actor import Actor
from rich.console import Console
from rich.table import Table
from rich import box
from rich.style import Style


FORMAT = '%(asctime)-15s %(filename)s - %(lineno)d - %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)
logger = logging.getLogger(__name__)


class Buddy:
    def __init__(self, streaming_service) -> None:
        self.base_props = BaseProperties()
        self.streaming_config = Streaming()
        self.genre_config = Genre()
        self.actor_config = Actor()
        self.streaming_service = streaming_service

    @property
    def streaming_service(self):
        return self._streaming_service

    @streaming_service.getter
    def streaming_service(self):
        return self._streaming_service

    @streaming_service.setter
    def streaming_service(self, val):
        if isinstance(val, str):
            self._streaming_service = val
        else:
            raise ValueError("Streaming service should be a string.")

    def movies_in_streaming(self, year="", genre_name="", actor_name=""):

        streaming_id = self.streaming_config.streaming_service_id(
            self.streaming_service)

        movies_by_service = self.streaming_config.movies_by_streaming_service(
            streaming_id,
            year,
            self.genre_config.genre_id_movie(genre_name),
            self.actor_config.actor_id(actor_name.replace(" ", "%20")))

        return movies_by_service.get("results")

    def tv_in_streaming(self, year="", genre_name=""):

        streaming_id = self.streaming_config.streaming_service_id(
            self.streaming_service)

        tv_by_service = self.streaming_config.tv_by_streaming_service(
            streaming_id,
            year,
            self.genre_config.genre_id_tv(genre_name))

        return tv_by_service.get("results")

    def display_table_movies(self, movies):
        table = Table(title=self.streaming_service,
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
                    cell_text = "https://image.tmdb.org/t/p/original"+cell_value
                    row[i] = cell_text
                else:
                    row[i] = cell_value

            table.add_row(*row)

        console = Console()
        console.print(table)

    def display_table_tv(self, tvs):
        table = Table(title=self.streaming_service,
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
                    cell_text = "https://image.tmdb.org/t/p/original"+cell_value
                    row[i] = cell_text
                else:
                    row[i] = cell_value

            table.add_row(*row)

        console = Console()
        console.print(table)


buddy_instance = Buddy(streaming_service="Netflix")
movies_data = buddy_instance.movies_in_streaming(
    genre_name="Comedy", year="", actor_name="")
buddy_instance.display_table_movies(movies_data)


# tv_data = buddy_instance.tv_in_streaming(
#     year="2022", genre_name="Comedy"
# )
# buddy_instance.display_table_tv(tv_data)
