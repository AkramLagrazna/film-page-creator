#create a class named movie to store movies info
class Movie():
    """ This class is built to store movies information """ 
    VALID_RATINGS = ['G','PG','PG-13','R']
    #__init__ is the first function called when the Movie class is called
    def __init__(self,movie_title, movie_storyline, poster_image, trailer_youtube):
        #define all internal functions
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    def show_trailer(self):
        import webbrowser
        webbrowser.open(self.trailer_youtube_url)
        
