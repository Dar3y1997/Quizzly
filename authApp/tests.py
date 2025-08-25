from django.test import TestCase

class Discount():
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def viewDetails(self):
        print(f"{self.name} {self.color} {self.price}")

car1 = Discount("Dodge", "Red", 50000000).viewDetails()


