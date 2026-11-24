class ElectronicDevice:
    def __init__(self, device_name, brand, model, price, warranty):
        self.device_name = device_name
        self.brand = brand
        self.model = model
        self.price = price
        self.warranty = warranty

    def details(self):
        print(f"Device Name : {self.device_name}")
        print(f"Brand       : {self.brand}")
        print(f"Model       : {self.model}")
        print(f"Price       : {self.price}")
        print(f"Warranty    : {self.warranty}")
        print("-" * 30)


device1 = ElectronicDevice("Smartphone", "Samsung", "Galaxy S24", 74999.0, "1 Year")
device2 = ElectronicDevice("Laptop", "Apple", "MacBook Air M3", 114900.0, "1 Year")
device3 = ElectronicDevice("Smartwatch", "Garmin", "Forerunner 265", 44990.0, "1 Year")
device4 = ElectronicDevice("Tablet", "Lenovo", "Tab P12", 26999.0, "1 Year")
device5 = ElectronicDevice("Wireless Earbuds", "Sony", "WF-1000XM5", 24990.0, "1 Year")

all_devices = [device1, device2, device3, device4, device5]

for d in all_devices:
    d.details()