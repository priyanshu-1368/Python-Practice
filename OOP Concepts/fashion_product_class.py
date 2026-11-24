class FashionProduct:
    def __init__(self, product_name, brand, size, color, price):
        self.product_name = product_name
        self.brand = brand
        self.size = size
        self.color = color
        self.price = price

    def details(self):
        print(f"Product Name : {self.product_name}")
        print(f"Brand        : {self.brand}")
        print(f"Size         : {self.size}")
        print(f"Color        : {self.color}")
        print(f"Price        : {self.price}")
        print("-" * 30)


fashion1 = FashionProduct("Oversized Cotton T-Shirt", "Zara", "L", "Black", 1299.0)
fashion2 = FashionProduct("Slim Fit Denim Jeans", "Levi's", "32", "Dark Blue", 2799.0)
fashion3 = FashionProduct("Floral Midi Dress", "H&M", "M", "Pastel Pink", 1999.0)
fashion4 = FashionProduct("Linen Casual Shirt", "Allen Solly", "XL", "White", 1650.0)
fashion5 = FashionProduct("Running Sneakers", "Nike", "9", "Grey", 4495.0)

all_fashion_products = [fashion1, fashion2, fashion3, fashion4, fashion5]

for f in all_fashion_products:
    f.details()