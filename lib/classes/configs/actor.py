import requests
from props.properties import BaseProperties
import logging
logger = logging.getLogger(__name__)


class Actor:
    def __init__(self) -> None:
        self.base_props = BaseProperties()
        pass

    def actor_id(self, actor_name):
        if isinstance(actor_name, str):
            try:
                actor_info = requests.get(
                    self.base_props.get_property(
                        'actor_config')+f"&query={actor_name}",
                    headers=self.base_props.get_property('tmdb_headers'))

                if actor_info.json()['results']:
                    return actor_info.json()['results'][0].get('id')
                else:
                    return
            except Exception as e:
                logger.error(e)
                return
        else:
            raise ValueError("actor_name should be a string.")
