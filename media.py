import webbrowser

#Movie Class used to create multiple instances with title, storyline, poster image, and trailer
class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        '''Constructor that requires instance variables (title, storyline, poster image, and trailer)'''
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        '''Instance Method that opens up a web browser'''
        webbrowser.open(self.trailer_youtube_url)
