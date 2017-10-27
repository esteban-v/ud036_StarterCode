import webbrowser


class Movie():
    """ This class creates instances of movies that will contain
        instance variables for each movie's title, storyline,
        poster_image_url and trailer_youtube_url """

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        """ This constructor initializes the required instance variables """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ This method opens the web browser with the url
            provided by the instance variable trailer_youtube_url
            to display the movie trailer """
        webbrowser.open(self.trailer_youtube_url)
