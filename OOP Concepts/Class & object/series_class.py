class WebSeries:
    def __init__(self, series_name, platform, seasons, genre, rating):
        self.series_name = series_name
        self.platform = platform
        self.seasons = seasons
        self.genre = genre
        self.rating = rating

    def details(self):
        print(f"Series Name : {self.series_name}")
        print(f"Platform    : {self.platform}")
        print(f"Seasons     : {self.seasons}")
        print(f"Genre       : {self.genre}")
        print(f"Rating      : {self.rating}")
        print("-" * 30)


series1 = WebSeries("Breaking Bad", "Netflix", 5, "Crime Drama", 9.5)
series2 = WebSeries("Game of Thrones", "JioCinema / HBO", 8, "Fantasy Drama", 9.2)
series3 = WebSeries("Dark", "Netflix", 3, "Sci-Fi Thriller", 8.7)
series4 = WebSeries("Moon Knight", "JioHotstar / Disney+", 1, "Action Fantasy", 7.3)
series5 = WebSeries("Loki", "JioHotstar / Disney+", 2, "Sci-Fi Fantasy", 8.2)

all_series = [series1, series2, series3, series4, series5]

for s in all_series:
    s.details()