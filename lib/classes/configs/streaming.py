import requests
from props.properties import BaseProperties
import logging
logger = logging.getLogger(__name__)


class Streaming:
    def __init__(self) -> None:
        self.base_props = BaseProperties()

    def streaming_service_id(self, name):

        try:
            streaming_services = requests.get(
                self.base_props.get_property('streaming_config'),
                headers=self.base_props.get_property('tmdb_headers'))

            streaming_dict = {item['provider_name']: item['provider_id']
                              for item in streaming_services.json()['results']}

            return [val for key, val in streaming_dict.items() if name in key][0]
        except Exception as e:
            logger.error(e)
            return

    def movies_by_streaming_service(self, streaming_id, year="", genre_id="", actor_id=""):

        try:
            streaming_services = requests.get(
                self.base_props.get_property(
                    'movie_streaming_endpoint') +
                f"&with_watch_providers={streaming_id}" +
                f"&primary_release_year={year}" +
                f"&with_genres={genre_id}" +
                f"&with_cast={actor_id}",
                headers=self.base_props.get_property('tmdb_headers'))

            return streaming_services.json()
        except Exception as e:
            logger.error(e)
            return

    def tv_by_streaming_service(self, streaming_id, year="", genre_id=""):

        try:
            streaming_services = requests.get(
                self.base_props.get_property(
                    'tv_streaming_endpoint') +
                f"&with_watch_providers={streaming_id}" +
                f"&first_air_date_year={year}" +
                f"&with_genres={genre_id}",
                headers=self.base_props.get_property('tmdb_headers'))

            return streaming_services.json()
        except Exception as e:
            logger.error(e)
            return
