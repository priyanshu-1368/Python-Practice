class Wedding:
    def __init__(self, bride_name, groom_name, wedding_date, location, total_guests):
        self.bride_name = bride_name
        self.groom_name = groom_name
        self.wedding_date = wedding_date
        self.location = location
        self.total_guests = total_guests

    def details(self):
        print(f"Bride : {self.bride_name}")
        print(f"Groom : {self.groom_name}")
        print(f"Date : {self.wedding_date}")
        print(f"Location : {self.location}")
        print(f"Guests : {self.total_guests}")
        print("-" * 30)


wedding_1 = Wedding("Aarohi", "Dev", "18-12-2026", "Rajkot", 450)
wedding_2 = Wedding("Nidhi", "Karan", "20-01-2027", "Ahmedabad", 300)
wedding_3 = Wedding("Priya", "Rohan", "04-02-2027", "Surat", 550)
wedding_4 = Wedding("Kavya", "Meet", "14-02-2027", "Vadodara", 350)
wedding_5 = Wedding("Diya", "Harsh", "27-02-2027", "Jamnagar", 250)

all_weddings = [wedding_1, wedding_2, wedding_3, wedding_4, wedding_5]

for w in all_weddings:
    w.details()
