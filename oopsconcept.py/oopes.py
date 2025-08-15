from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def get_fuel_efficiency(self):
        pass


class Car(Vehicle):
    def __init__(self, brand, year, num_doors):
        super().__init__(brand, year)
        self.num_doors = num_doors

    def start_engine(self):
        print(f"{self.brand} car engine started with a key.")

    def get_fuel_efficiency(self):
        return 15  # km per litre for example


class Bike(Vehicle):
    def __init__(self, brand, year):
        super().__init__(brand, year)

    def start_engine(self):
        print(f"{self.brand} bike engine started with a kick!")

    def get_fuel_efficiency(self):
        return 80  # km per litre
class Truck(Vehicle):
    def __init__(self, brand, year, capacity):
        super().__init__(brand, year)
        self.capacity = capacity
    def start_engine(self):
        print(f"{self.brand} truck engine started with a key .{self.capacity} tons capacity")
    def get_fuel_efficiency(self):
        return 10  # km per litre
vehicles = [
    Car("Toyota", 2020, 4),
    Bike("Honda", 2018),
    Truck("Benz", 2015, 10),
    Car("Ford", 2019, 2),
    Truck("Tata", 2019, 5),
    Bike("Yamaha", 2021)
]
for vehicle in vehicles:
    vehicle.start_engine()
    effiency=vehicle.get_fuel_efficiency()
    print(f"Fuel efficiency of {vehicle.brand} is {effiency} km/litr")