class Car:
    def __init__(self, car_name, brand, fuel_type, mileage, price):
        self.car_name = car_name
        self.brand = brand
        self.fuel_type = fuel_type
        self.mileage = mileage
        self.price = price

    def details(self):
        print(f"Car Name  : {self.car_name}")
        print(f"Brand     : {self.brand}")
        print(f"Fuel Type : {self.fuel_type}")
        print(f"Mileage   : {self.mileage}")
        print(f"Price     : {self.price}")
        print("-" * 30)


car1 = Car("Swift", "Maruti Suzuki", "Petrol", "24.8 km/l", 649000.0)
car2 = Car("Creta", "Hyundai", "Diesel", "21.8 km/l", 1450000.0)
car3 = Car("Nexon EV", "Tata", "Electric", "465 km/charge", 1599000.0)
car4 = Car("Thar Roxx", "Mahindra", "Diesel", "15.2 km/l", 1799000.0)
car5 = Car("Fortuner", "Toyota", "Diesel", "14.4 km/l", 3599000.0)

all_cars = [car1, car2, car3, car4, car5]

for c in all_cars:
    c.details()