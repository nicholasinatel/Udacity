# File Storing for The Classes used in the website
import webbrowser


class Movie():
    # __doc__ variable
    """Movie class with attributes.

    This class provides the proper variables to,
    arrange and organize a list of movies that
    can be shown in an HTML page.

    Attributes:
        title: Movie Title
        poster_image_url: An online image to be displayed
        trailer_youtube_url: Youtube link to be played in webbrowser
    """
    # Constructor 
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        """Inits MovieClass with its 3 attributes."""
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    # Method for showing Trailer
    def show_trailer(self):
        """Opens WebBrowser with given youtube URL.

        From webbrowser module, call function that opens the default webbrowser
        from system and automatically play the trailer throw it's id.

        Args:
            self: Movie Instance Name being called

        Returns:
            Nothing

        Raises:
            Error: Video Unavailable
        """
        webbrowser.open(self.trailer_youtube_url)
