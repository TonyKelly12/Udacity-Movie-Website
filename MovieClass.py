import webbrowser

class Movie():
  """ This class sets up the movie data in the format needed to post to html""" 
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """ this init takes in the movie title, the description or storyline, the movie poster 
        and the youtube trailer url"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

        def show_trailer(self):
            webbrowser.open(self.trailer_youtube_url)


    