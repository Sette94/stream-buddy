import requests
from props.properties import BaseProperties
import logging
logger = logging.getLogger(__name__)


class Genre:
    def __init__(self) -> None:
        self.base_props = BaseProperties()
        pass

    def movie_genre(self):
        try:
            genres = requests.get(
                self.base_props.get_property('movie_genre_config'),
                headers=self.base_props.get_property('tmdb_headers'))

            genre_dict = {item['name']: item['id']
                          for item in genres.json()['genres']}

            return genre_dict
        except Exception as e:
            logger.error(e)
            return

    def tv_genre(self):
        try:
            genres = requests.get(
                self.base_props.get_property('tv_genre_config'),
                headers=self.base_props.get_property('tmdb_headers'))

            genre_dict = {item['name']: item['id']
                          for item in genres.json()['genres']}
            return genre_dict
        except Exception as e:
            logger.error(e)
            return

    def genre_id_tv(self, genre_name):
        if isinstance(genre_name, str):
            try:
                return self.tv_genre().get(genre_name)
            except Exception as e:
                logger.error(e)
                return
        else:
            raise ValueError("genre name should be a string.")

    def genre_id_movie(self, genre_name):
        if isinstance(genre_name, str):
            try:
                return self.movie_genre().get(genre_name)
            except Exception as e:
                logger.error(e)
                return
        else:
            raise ValueError("genre name should be a string.")
