class OnlineOrder:
    def __init__(self, order_id, customer_name, order_date, total_amount, payment_status):
        self.order_id = order_id
        self.customer_name = customer_name
        self.order_date = order_date
        self.total_amount = total_amount
        self.payment_status = payment_status

    def details(self):
        print(f"Order ID       : {self.order_id}")
        print(f"Customer Name  : {self.customer_name}")
        print(f"Order Date     : {self.order_date}")
        print(f"Total Amount   : {self.total_amount}")
        print(f"Payment Status : {self.payment_status}")
        print("-" * 30)


order1 = OnlineOrder("ORD-101", "Aarav Patel", "24-11-2026", 1499.0, "Pending")
order2 = OnlineOrder("ORD-102", "Neha Shah", "24-11-2026", 299.0, "Paid")
order3 = OnlineOrder("ORD-103", "Rohan Desai", "24-11-2026", 850.0, "Failed")
order4 = OnlineOrder("ORD-104", "Pooja Mehta", "24-11-2026", 2400.0, "Paid")
order5 = OnlineOrder("ORD-105", "Karan Joshi", "24-11-2026", 620.0, "Pending")

all_orders = [order1, order2, order3, order4, order5]

for o in all_orders:
    o.details()