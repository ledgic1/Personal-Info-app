class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        self.started = False

    def start_engine(self):
        if not self.started:
            print(f"{self.brand} engine started!")
            self.started = True
        else:
            print(f" The {self.brand} is already running.")
    def car_driving(self):
        if self.started:
            print(f"The {self.brand} is driving down the road")
            self.started = True
        else:
            print(f"{self.brand} you need to start the car")

    def stop_engine(self):
        if self.started:
            print(f"{self.brand} engine stopped.")
            self.started = False
        else:
            print(f"{self.brand} is already off.")

# Using the class
my_car = Car("Toyota", 2022)
my_car.start_engine()
my_car.car_driving()
my_car.stop_engine()
