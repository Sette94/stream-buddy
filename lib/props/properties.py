class BaseProperties:

    props_container = {}

    def __init__(self):
        self.props_container['bearer'] = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkNGRiOWVjMDVkOGRjYTRiOTY0NDI4NDJiNzc3MTljMSIsInN1YiI6IjY1OTJlYmNkNTFhNjRlMDNiNWY0OTJjNSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.PCjHmysZK7nS4Rd8KGNlEKaDha-TIB0783l5XyVq8HQ"
        self.props_container['streaming_config'] = "https://api.themoviedb.org/3/watch/providers/movie?language=en-US&watch_region=US"
        self.props_container['movie_genre_config'] = "https://api.themoviedb.org/3/genre/movie/list?language=en"
        self.props_container['tv_genre_config'] = "https://api.themoviedb.org/3/genre/tv/list?language=en"
        self.props_container['actor_config'] = "https://api.themoviedb.org/3/search/person?include_adult=false&language=en-US&page=1"

        self.props_container['movie_streaming_endpoint'] = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=vote_count.desc&watch_region=US&with_watch_monetization_types=flatrate&with_original_language=en"
        self.props_container['tv_streaming_endpoint'] = "https://api.themoviedb.org/3/discover/tv?include_adult=false&include_null_first_air_dates=false&language=en-US&page=1&sort_by=popularity.desc&with_original_language=en"

        self.props_container['tmdb_headers'] = {
            "accept": "application/json",
            "Authorization": f"Bearer {self.get_property('bearer')}"
        }

    def properties(self):
        return self.props_container

    def get_property(self, key):
        return self.props_container.get(key, None)
