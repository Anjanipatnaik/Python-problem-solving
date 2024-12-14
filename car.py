class car():
    def __init__(self,brand,fuel_type,mileage):
        self.brand = brand
        self.fuel_type = fuel_type
    def
class fuelcar(car):
    def __init__(self,brand,battery_capacity,range_per_change):
        super(). __init__(brand)
        self.battery_capacity = battery_capacity
        self.range_per_change = range_per_change
    def drive(self):
        print(f"{self.brand} has a battery capacity of {self.battery_capacity} kmh and a range of {self.range_per_change} km per charge.")
car1 = FuelCar(brand = "BMW",battery_capacity = "3 months")
