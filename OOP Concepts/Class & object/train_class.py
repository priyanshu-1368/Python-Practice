class Train:
    def __init__(self, train_number, train_name, source, destination, ticket_price):
        self.train_number = train_number
        self.train_name = train_name
        self.source = source
        self.destination = destination
        self.ticket_price = ticket_price

    def details(self):
        print(f"Train Number : {self.train_number}")
        print(f"Train Name   : {self.train_name}")
        print(f"Source       : {self.source}")
        print(f"Destination  : {self.destination}")
        print(f"Ticket Price : {self.ticket_price}")
        print("-" * 30)


train1 = Train("12957", "Swarna Jayanti Rajdhani", "New Delhi", "Ahmedabad", 2850.0)
train2 = Train("22945", "Saurashtra Mail", "Mumbai Central", "Okha", 790.0)
train3 = Train("19209", "Somnath Express", "Ahmedabad", "Veraval", 340.0)
train4 = Train("12267", "Mumbai Central Duronto", "Mumbai Central", "Ahmedabad", 1920.0)
train5 = Train("22955", "Kutch Express", "Bandra Terminus", "Bhuj", 685.0)

all_trains = [train1, train2, train3, train4, train5]

for t in all_trains:
    t.details()