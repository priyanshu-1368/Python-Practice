class Pharmacy:
    def __init__(self, medicine_name, company_name, medicine_type, price, expiry_date):
        self.medicine_name = medicine_name
        self.company_name = company_name
        self.medicine_type = medicine_type
        self.price = price
        self.expiry_date = expiry_date

    def details(self):
        print(f"Medicine Name : {self.medicine_name}")
        print(f"Company Name  : {self.company_name}")
        print(f"Medicine Type : {self.medicine_type}")
        print(f"Price         : {self.price}")
        print(f"Expiry Date   : {self.expiry_date}")
        print("-" * 30)


medicine1 = Pharmacy("Dolo 650", "Micro Labs", "Tablet", 32.0, "15-08-2028")
medicine2 = Pharmacy("Benadryl", "Johnson & Johnson", "Syrup", 128.0, "10-11-2027")
medicine3 = Pharmacy("Azithral 500", "Alembic", "Tablet", 119.5, "22-05-2028")
medicine4 = Pharmacy("Betadine", "Win-Medicare", "Ointment", 145.0, "30-01-2028")
medicine5 = Pharmacy("Pantocid DSR", "Sun Pharma", "Capsule", 210.0, "18-09-2027")

all_medicines = [medicine1, medicine2, medicine3, medicine4, medicine5]

for m in all_medicines:
    m.details()