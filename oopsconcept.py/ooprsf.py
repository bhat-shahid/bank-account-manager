from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self, brand, year):
        self.brand=brand
        self.year=year
        self.rented=False
    @abstractmethod
    def rent():
        pass
    def return_vehicle():
        pass
    def calculate_rent(self,days):
        pass
class Car(Vehicle):
    def __init__(self, brand, year, daily_rate):
        super().__init__(brand, year,)
        self.daily_rate=daily_rate
    def rent(self):
        if self.rented:
            print(f"{self.brand} car is already rented.")
        else:
            self.rented=True
            print(f"{self.brand} car has been rented.")
    def return_vehicle(self):
        if not self.rented:
            print(f"{self.brand} car was not rented.")
        else:
            self.rented=False
            print(f"{self.brand} car has been returned.")
    def calculate_rent(self,days):
        return self.daily_rate*days
class Bike(Vehicle):
    def __init__(self, brand, year,daily_rate):
        super().__init__(brand, year)
        self.daily_rate=daily_rate
    def rent(self):
        if self.rented:
            print(f"{self.brand} Bike is already rented.")
        else:
            self.rented=True
            print(f"{self.brand} Bike has been rented.")
    def return_vehicle(self):
        if not self.rented:
            print(f"{self.brand} Bike was not rented.")
        else:
            self.rented=False
            print(f"{self.brand} Bike has been returned.")
    def calculate_rent(self,days):
        return self.daily_rate*days
class Truck(Vehicle):
    def __init__(self, brand, year,daily_rate, capacity):
        super().__init__(brand, year)
        self.daily_rate=daily_rate
        self.capacity=capacity
    def rent(self):
        if self.rented:
            print(f"{self.brand} Truck is already rented.")
        else:
            self.rented=True
            print(f"{self.brand} Truck has been rented.")
    def return_vehicle(self):
        if not self.rented:
            print(f"{self.brand} Truck was not rented.")
        else:
            self.rented=False
            print(f"{self.brand} Truck has been returned.")
    def calculate_rent(self,days):
        return self.daily_rate*days*self.capacity
    
vehciles=[
    Car("Toyota",2015,50),
    Bike("Honda",2018,20),
    Truck("Ford",2012,30,5)
]
for vehicle in vehciles:
    vehicle.rent()
    vehicle.return_vehicle()
    vehicle.calculate_rent(10)
    rented_on_days=vehicle.calculate_rent(10)
    print(f"Total rent for in days: {rented_on_days}")