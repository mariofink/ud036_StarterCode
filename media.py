class Movie:
    """Stores movie information """

    def __init__(self, title, poster, trailer_youtube_url):
        """Store the following information for a movie object
        * title
        * an url of an image of the movie’s poster
        * an url linking to a movie trailer on YouTube
        """
        self.title = title
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer_youtube_url
