import fresh_tomatoes

class Movie(object):
    def __init__(self, title, trailer_url, poster_url):
        self.title = title
        self.trailer_youtube_url = trailer_url
        self.poster_image_url = poster_url
    
    @staticmethod
    def from_string(movieString):
        """
        Create a Movie from a string
        Format: title, then trailer url, then poster url, separated by newlines
        """
        newMovie = Movie(None, None, None)
        attributes = movieString.split("\n")
        newMovie.title = attributes[0].strip()
        newMovie.trailer_youtube_url = attributes[1].strip()
        newMovie.poster_image_url = attributes[2].strip()
        return newMovie
    
    @staticmethod
    def from_file(filename):
        """
        Create a Movie from a file
        Format: title, then trailer url, then poster url, separated by newlines
        """
        with open(filename, "r") as movieFile:
            movieString = movieFile.read()
        return Movie.from_string(movieString)
        

def main():
    # Create movies list
    movies = [ Movie.from_file("Troll_2.txt"),
               Movie.from_file("Birdemic.txt"),
               Movie.from_file("The_Room.txt")
             ]
    
    # Open page
    fresh_tomatoes.open_movies_page(movies)


if __name__ == "__main__":
    main()