class Restaurant:
    def __init__(self, restaurant_name, location, rating, food_type, contact_number):
        self.restaurant_name = restaurant_name
        self.location = location
        self.rating = rating
        self.food_type = food_type
        self.contact_number = contact_number

    def details(self):
        print(f"Restaurant Name : {self.restaurant_name}")
        print(f"Location        : {self.location}")
        print(f"Rating          : {self.rating}")
        print(f"Food Type       : {self.food_type}")
        print(f"Contact Number  : {self.contact_number}")
        print("-" * 30)


restaurant1 = Restaurant("Lords Banquet & Dining", "Rajkot", 4.5, "Gujarati & North Indian", "+91-281-2451122")
restaurant2 = Restaurant("Agashiye", "Ahmedabad", 4.7, "Traditional Gujarati Thali", "+91-79-25506980")
restaurant3 = Restaurant("Little Italy", "Surat", 4.4, "Italian & Continental", "+91-261-2234567")
restaurant4 = Restaurant("Mandap", "Vadodara", 4.3, "Multi-Cuisine", "+91-265-2345678")
restaurant5 = Restaurant("Kesar Vilas Palace", "Jamnagar", 4.2, "Kathiyawadi & Royal", "+91-288-2553310")

all_restaurants = [restaurant1, restaurant2, restaurant3, restaurant4, restaurant5]

for r in all_restaurants:
    r.details()