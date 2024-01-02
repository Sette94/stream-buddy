class BaseProperties:

    props_container = {}

    def __init__(self):
        self.props_container['bearer'] = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkNGRiOWVjMDVkOGRjYTRiOTY0NDI4NDJiNzc3MTljMSIsInN1YiI6IjY1OTJlYmNkNTFhNjRlMDNiNWY0OTJjNSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.PCjHmysZK7nS4Rd8KGNlEKaDha-TIB0783l5XyVq8HQ"
        self.props_container['streaming_config'] = "https://api.themoviedb.org/3/watch/providers/movie?language=en-US&watch_region=US"
        self.props_container['streaming_endpoint'] = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=vote_count.desc&watch_region=US&with_watch_monetization_types=flatrate"

        # Use self.get_property('bearer') instead of self.base_props.get_property('bearer')
        self.props_container['tmdb_headers'] = {
            "accept": "application/json",
            "Authorization": f"Bearer {self.get_property('bearer')}"
        }

    def properties(self):
        return self.props_container

    def get_property(self, key):
        return self.props_container.get(key, None)
