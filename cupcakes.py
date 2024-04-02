import csv
from pprint import pprint
from abc import ABC, abstractmethod

class Cupcake(ABC):
    size = "Regular"

    def __init__(self, name, price, flavor, frosting, filling):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.filling = filling
        self.sprinkles = []

    def add_sprinkles(self, *args):
        for sprinkle in args:
            self.sprinkles.append(sprinkle)
        
    @abstractmethod 
    def calculate_price(self, quantity):
        return quantity * self.price
    
class Mini(Cupcake):
    size = "Mini"

    def __init__(self, name, price, flavor, frosting):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting 
        self.sprinkles = []

    def calculate_price(self, quantity):
        return quantity * self.price

class Regular(Cupcake):
    size = "Regular"

    def __init__(self, name, price, flavor, frosting, filling):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.filling = filling
        self.sprinkles = []

    def calculate_price(self, quantity):
        return quantity * self.price

class Large(Cupcake):
    size = "Large"

    def __init__(self, name, price, flavor, frosting, filling):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.filling = filling
        self.sprinkles = []

    def calculate_price(self, quantity):
        return quantity * self.price

cupcake_one = Regular("Chocolate", 2.99, "Chocolate", "Buttercream", None)
cupcake_two = Mini("Vanilla", 0.99, "Vanilla", "Chocolate")
cupcake_three = Large("Vanilla", 1.99, "Vanilla", "Marshmello", "Chocolate")
cupcake_four = Regular("Patriot", 3.59, "Vanilla", "Red Velvet", "Blueberry")
cupcake_four.add_sprinkles("Red", "White", "Blue")
cupcake_five = Regular("Choco-Bomb", 3.99, "Chocolate", "Chocolate", "Chocolate")
cupcake_five.add_sprinkles("Chocolate")

cupcake_list = [cupcake_one, cupcake_two, cupcake_three, cupcake_four, cupcake_five]

def write_new_csv(file, cupcakes):
    with open(file, "w", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

    for cupcake in cupcakes:
        if hasattr(cupcake, "filling"):
            writer.writerow(
                {"size": cupcake.size, 
                "name": cupcake.name, 
                "price": cupcake.price, 
                "flavor": cupcake.flavor, 
                "frosting": cupcake.frosting, 
                "filling": cupcake.filling, 
                "sprinkles": cupcake.sprinkles
                })
        else:
            writer.writerow(
                {"size": cupcake.size, 
                "name": cupcake.name, 
                "price": cupcake.price, 
                "flavor": cupcake.flavor, 
                "frosting": cupcake.frosting, 
                "sprinkles": cupcake.sprinkles
                })

def append_csv(file, cupcakes):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        for cupcake in cupcakes:
            if hasattr(cupcake, "filling"):
                writer.writerow(
                    {"size": cupcake.size, 
                    "name": cupcake.name, 
                    "price": cupcake.price, 
                    "flavor": cupcake.flavor, 
                    "frosting": cupcake.frosting, 
                    "filling": cupcake.filling, 
                    "sprinkles": cupcake.sprinkles
                    })
            else:
                writer.writerow(
                    {"size": cupcake.size, 
                    "name": cupcake.name, 
                    "price": cupcake.price, 
                    "flavor": cupcake.flavor, 
                    "frosting": cupcake.frosting, 
                    "sprinkles": cupcake.sprinkles
                    })
            
def get_cupcakes(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        reader = list(reader)
        return reader

def find_cupcake(file, name):
    for cupcake in get_cupcakes(file):
        if cupcake["name"] == name:
            return cupcake
    return None

def add_cupcake_dictionary(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(cupcake)

def read_csv(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            pprint(row)

