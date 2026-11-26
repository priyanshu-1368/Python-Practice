class Product:
    def __init__(self, product_id, product_name, category, price, quantity):
        self.product_id = product_id
        self.product_name = product_name
        self.category = category
        self.price = price
        self.quantity = quantity

    def details(self):
        print(f"Product ID   : {self.product_id}")
        print(f"Product Name : {self.product_name}")
        print(f"Category     : {self.category}")
        print(f"Price        : {self.price}")
        print(f"Quantity     : {self.quantity}")
        print("-" * 30)


product1 = Product("PRD-201", "Basmati Rice 5kg", "Groceries", 640.0, 25)
product2 = Product("PRD-202", "Stainless Steel Bottle", "Kitchen", 499.0, 40)
product3 = Product("PRD-203", "Desk Lamp", "Home Decor", 899.0, 15)
product4 = Product("PRD-204", "Notebook Pack of 6", "Stationery", 270.0, 60)
product5 = Product("PRD-205", "Electric Kettle", "Appliances", 1350.0, 18)

all_products = [product1, product2, product3, product4, product5]

for pr in all_products:
    pr.details()