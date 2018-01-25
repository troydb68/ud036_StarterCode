import webbrowser


class Movie():
    '''
    Movie Class used to create multiple instances with title,
    storyline, poster image, and trailer.
    '''

    def __init__(self, movie_title, movie_story, poster_image, movie_trailer):
        '''
        Constructor that requires instance variables
        (title, storyline, poster image, and trailer)
        '''
        self.title = movie_title
        self.storyline = movie_story
        self.poster_image_url = poster_image
        self.trailer_youtube_url = movie_trailer

    def show_trailer(self):
        '''Instance Method that opens up a web browser'''
        webbrowser.open(self.trailer_youtube_url)
