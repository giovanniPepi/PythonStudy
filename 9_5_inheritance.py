class Car:

    """A simple attempt to represent a car."""

    def __init__(self, manufacturer, model, year):
        """Initialize attributes to describe a car."""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year        
        self.odometer_reading = 0 
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Prints how many km the car has run"""
        print(f"This car has {self.odometer_reading} km on it.")
    
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value
        Rejec the change if it attempts to roll the odometer back.
        """
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print(f"You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
        
class Battery:
    """Attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributers."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement to describe the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self): 
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        
        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        
        if self.battery_size <= 100:
            print(f"Upgrading battery from {self.battery_size} to 100 kWh.")
            self.battery_size = 100
        elif self.battery_size == 100:
            print(f"Your car has a {self.battery_size} kWh battery, the biggest size we can offer.")




class ElectricCar(Car):
    """Represent aspects of a car, specific to eletric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        
        # super is used to call the method from parent class
        super().__init__(make, model, year) 
        # This line tells Python to create a new instance of Battery
        self.battery = Battery()
    def fill_gas_tank(self):
        """Eletric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")            

my_tesla = ElectricCar('tesla', 'model s', '2019')
print(my_tesla.get_descriptive_name())

# This line tells Python to look at the instance my_tesla, find its battery attribute, 
#  and call the method describe_battery()

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

car1 = ElectricCar('nissan', 'Leaf', '2020')
print(car1.get_descriptive_name())
car1.battery.describe_battery()
car1.battery.get_range()
car1.battery.upgrade_battery()
car1.battery.get_range()



