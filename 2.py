class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

class ElectricCar(Vehicle):
    def __init__(self, brand, speed, battery):
        super().__init__(brand, speed)
        self.battery = battery
        
    def describe(self):
        print(f"Brand: {self.brand}, Speed: {self.speed}, Battery: {self.battery}")

car = ElectricCar("Tesla", 250, "100 kWh")
car.describe()