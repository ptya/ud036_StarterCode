class Movie():
    """ This class provides a way to store movie related information

    Attributes:
        title: The title of the movie.
        poster_image: URL to the poster image of the movie.
        trailer_youtube_url: URL to the trailer of the movie.
    """

    def __init__(self, movie_title, poster_image,
                 trailer_youtube):
        """Inits Movie with required information."""
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
