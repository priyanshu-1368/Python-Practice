class Game:
    def __init__(self, game_name, game_type, developer, release_year, price):
        self.game_name = game_name
        self.game_type = game_type
        self.developer = developer
        self.release_year = release_year
        self.price = price

    def details(self):
        print(f"Game Name    : {self.game_name}")
        print(f"Game Type    : {self.game_type}")
        print(f"Developer    : {self.developer}")
        print(f"Release Year : {self.release_year}")
        print(f"Price        : {self.price}")
        print("-" * 30)


game1 = Game("Grand Theft Auto V", "Action Adventure", "Rockstar North", 2013, 1499.0)
game2 = Game("Cyberpunk 2077", "RPG", "CD Projekt Red", 2020, 2999.0)
game3 = Game("Red Dead Redemption 2", "Open World Action", "Rockstar Games", 2018, 2499.0)
game4 = Game("The Last of Us Part I", " Action-Adventure and Survival Horror", "Naughty Dog", 2022, 1999.50)
game5 = Game("Elden Ring", "Action RPG", "FromSoftware", 2022, 3599.0)

all_games = [game1, game2, game3, game4, game5]

for g in all_games:
    g.details()