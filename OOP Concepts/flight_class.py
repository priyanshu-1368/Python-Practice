class Flight:
    def __init__(self, flight_number, airline_name, source, destination, ticket_price):
        self.flight_number = flight_number
        self.airline_name = airline_name
        self.source = source
        self.destination = destination
        self.ticket_price = ticket_price

    def details(self):
        print(f"Flight Number : {self.flight_number}")
        print(f"Airline Name  : {self.airline_name}")
        print(f"Source        : {self.source}")
        print(f"Destination   : {self.destination}")
        print(f"Ticket Price  : {self.ticket_price}")
        print("-" * 30)


flight1 = Flight("6E-5012", "IndiGo", "Ahmedabad", "Bengaluru", 5450.0)
flight2 = Flight("AI-887", "Air India", "Mumbai", "Delhi", 4890.0)
flight3 = Flight("QP-1124", "Akasa Air", "Surat", "Goa", 3650.0)
flight4 = Flight("UK-945", "Air India", "Delhi", "Hyderabad", 6120.0)
flight5 = Flight("6E-219", "IndiGo", "Rajkot", "Mumbai", 3290.0)

all_flights = [flight1, flight2, flight3, flight4, flight5]

for fl in all_flights:
    fl.details()