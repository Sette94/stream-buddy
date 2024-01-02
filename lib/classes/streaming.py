import requests
from properties import BaseProperties
import logging
logger = logging.getLogger(__name__)


class Streaming:
    def __init__(self) -> None:
        self.base_props = BaseProperties()

    def streaming_service(self, name):

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

    def movies_by_streaming_service(self, streaming_id, year=""):

        try:
            streaming_services = requests.get(
                self.base_props.get_property(
                    'streaming_endpoint')+f"&with_watch_providers={streaming_id}"+f"&primary_release_year={year}",
                headers=self.base_props.get_property('tmdb_headers'))

            logger.info(self.base_props.get_property(
                'streaming_endpoint')+f"&with_watch_providers={streaming_id}")

            return streaming_services.json()
        except Exception as e:
            logger.error(e)
            return
