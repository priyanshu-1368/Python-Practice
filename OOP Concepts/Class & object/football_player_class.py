class FootballPlayer:
    def __init__(self, player_name, age, country, position, jersey_number):
        self.player_name = player_name
        self.age = age
        self.country = country
        self.position = position
        self.jersey_number = jersey_number

    def details(self):
        print(f"Player Name   : {self.player_name}")
        print(f"Age           : {self.age}")
        print(f"Country       : {self.country}")
        print(f"Position      : {self.position}")
        print(f"Jersey Number : {self.jersey_number}")
        print("-" * 30)


player1 = FootballPlayer("Lionel Messi", 39, "Argentina", "Forward", 10)
player2 = FootballPlayer("Cristiano Ronaldo", 41, "Portugal", "Striker", 7)
player3 = FootballPlayer("Kylian Mbappe", 27, "France", "Forward", 9)
player4 = FootballPlayer("Kevin De Bruyne", 35, "Belgium", "Midfielder", 17)
player5 = FootballPlayer("Sunil Chhetri", 42, "India", "Forward", 11)

all_players = [player1, player2, player3, player4, player5]

for p in all_players:
    p.details()