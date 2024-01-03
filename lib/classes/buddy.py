import logging
from properties import BaseProperties
from streaming import Streaming
from genre import Genre
from actor import Actor
from rich.console import Console
from rich.table import Table
from rich import box


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

        # Returns an id for the initalized streaming service (Netflix = 8)
        streaming_id = self.streaming_config.streaming_service_id(
            self.streaming_service)

        # genre_config.genre_id(genre_name) like streaming_config.streaming_service_id takes a genre name and returns an id
        # Returns a list of object, movies based on streaming_id, released year, genre_id
        movies_by_service = self.streaming_config.movies_by_streaming_service(
            streaming_id,
            year,
            self.genre_config.genre_id(genre_name),
            self.actor_config.actor_id(actor_name.replace(" ", "%20")))

        # for movie in movies_by_service.get("results"):
        #     logger.info(movie.get('original_title')+": "+movie.get('overview'))

        return movies_by_service.get("results")

    def display_table(self, movies):
        table = Table(title=self.streaming_service,
                      box=box.HEAVY, show_lines=True)

        rows = [
            [movie.get('original_title', 'N/A'), movie.get('overview',
                                                           'N/A'), movie.get('release_date', 'N/A')]
            for movie in movies
        ]

        columns = ["Title", "Overview", "Release Date"]

        for column in columns:
            table.add_column(column, justify="center", style="red")

        for row in rows:
            table.add_row(*row)

        console = Console()
        console.print(table)


buddy_instance = Buddy(streaming_service="Netflix")
movies_data = buddy_instance.movies_in_streaming(
    genre_name="", year="2018")
buddy_instance.display_table(movies_data)
