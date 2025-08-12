# Base class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"{self.brand} {self.model}"

# Smartphone class inheriting from Device
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery_life):
        super().__init__(brand, model)  # Call the parent constructor
        self.storage = storage
        self.battery_life = battery_life

    def make_call(self, number):
        print(f"Calling {number} from {self.device_info()}...")

    def browse_internet(self):
        print(f"Browsing the internet on {self.device_info()}...")

    def phone_info(self):
        return f"{self.device_info()} | Storage: {self.storage}GB | Battery: {self.battery_life}hrs"

# Example usage
phone1 = Smartphone("Apple", "iPhone 15", 256, 20)
phone2 = Smartphone("Samsung", "Galaxy S24", 512, 25)

print(phone1.phone_info())
phone1.make_call("123-456-7890")
phone1.browse_internet()

print(phone2.phone_info())
phone2.make_call("987-654-3210")

#Polymorphism Challenge!
# Base class
class Vehicle:
    def move(self):
        pass  # To be defined by subclasses

# Subclass: Car
class Car(Vehicle):
    def move(self):
        print("Driving ")

# Subclass: Plane
class Plane(Vehicle):
    def move(self):
        print("Flying ")

# Subclass: Boat
class Boat(Vehicle):
    def move(self):
        print("Sailing ")

# Function to demonstrate polymorphism
def start_journey(vehicles):
    for vehicle in vehicles:
        vehicle.move()

# Create objects
car = Car()
plane = Plane()
boat = Boat()

# List of vehicles
vehicles = [car, plane, boat]

# Start the journey (polymorphism in action)
start_journey(vehicles)