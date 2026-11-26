class CricketPlayer:
    def __init__(self, player_name, country, age, total_runs, role):
        self.player_name = player_name
        self.country = country
        self.age = age
        self.total_runs = total_runs
        self.role = role

    def details(self):
        print(f"Player Name : {self.player_name}")
        print(f"Country     : {self.country}")
        print(f"Age         : {self.age}")
        print(f"Total Runs  : {self.total_runs}")
        print(f"Role        : {self.role}")
        print("-" * 30)


player1 = CricketPlayer("Virat Kohli", "India", 38, 26733, "Batsman")
player2 = CricketPlayer("Rohit Sharma", "India", 39, 18847, "Opening Batsman")
player3 = CricketPlayer("Ravindra Jadeja", "India", 37, 6245, "All-Rounder")
player4 = CricketPlayer("Ben Stokes", "England", 35, 9612, "All-Rounder")
player5 = CricketPlayer("Pat Cummins", "Australia", 33, 1890, "Bowler")

all_cricket_players = [player1, player2, player3, player4, player5]

for cp in all_cricket_players:
    cp.details()