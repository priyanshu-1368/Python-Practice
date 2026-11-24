class Movie:
    def __init__(self, movie_name, director, release_year, rating, language):
        self.movie_name = movie_name
        self.director = director
        self.release_year = release_year
        self.rating = rating
        self.language = language

    def details(self):
        print(f"Movie Name   : {self.movie_name}")
        print(f"Director     : {self.director}")
        print(f"Release Year : {self.release_year}")
        print(f"Rating       : {self.rating}")
        print(f"Language     : {self.language}")
        print("-" * 30)


movie1 = Movie("Inception", "Christopher Nolan", 2010, 8.8, "Hindi, English")
movie2 = Movie("Avengers: Endgame", "Anthony & Joe Russo", 2019, 8.4, "Hindi, English")
movie3 = Movie("John Wick", "Chad Stahelski", 2014, 7.5, "Hindi, English")
movie4 = Movie("The Odyssey", "Christopher Nolan", 2026, 8.5, "Hindi, English")
movie5 = Movie("F**** C***", "David Fincher", 1999, 8.8, "Hindi, English")

all_movies = [movie1, movie2, movie3, movie4, movie5]

for mv in all_movies:
    mv.details()