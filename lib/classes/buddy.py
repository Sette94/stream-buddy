import logging

from properties import BaseProperties
from streaming import Streaming

FORMAT = '%(asctime)-15s %(filename)s - %(lineno)d - %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)
logger = logging.getLogger(__name__)


class Buddy:
    def __init__(self, streaming_service) -> None:
        self.base_props = BaseProperties()
        self.streaming_config = Streaming()
        self.streaming_service = ""

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

    def movies_in_streaming(self, year=""):

        streaming_id = self.streaming_config.streaming_service(
            self.streaming_service)
        logger.info(streaming_id)

        movies_by_service = self.streaming_config.movies_by_streaming_service(
            streaming_id, year)

        logger.info(movies_by_service)

        return movies_by_service


buddy_instance = Buddy(streaming_service="Netflix")
buddy_instance.movies_in_streaming(2000)
