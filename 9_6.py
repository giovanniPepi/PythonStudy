
class Restaurant:
    """Places you can eat"""

    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.number_served = 0
    
    def describe_restaurant(self):
        """Gives information about places human can eat"""
        print(f"This restaurant is called {self.name} and is of the {self.type} kind.")
    
    def open_restaurant(self):
        """Warns humans that the place is open"""
        print(f"{self.name} is now open.")
    
    def read_served(self):
        """Reads how many clients were served"""
        print(f"{self.number_served} clients served. ")

    def set_number_served(self, number_served):
        """Keeps track of how many customers were served."""
        self.number_served = number_served
        print(f"{self.number_served} clients served.")
    
    def increment_number_served(self, increment):
        """Increase the client count"""
        self.number_served += increment
        print(f"{self.number_served} clients served.")


class Icecream(Restaurant):

    def __init__(self, name, type):
        super().__init__(name, type)
    
    def describeflavors(self):
        """Describe ice cream flavors on the menu."""
        flavors = ['ninho trufado', 'chocolate', 'leite', 'pistache']
        
        for flavor in flavors:
            print(f"{flavor.title()} is available.")
              


restaurant1 = Restaurant('Olive Garden', 'Italian')
restaurant2 = Restaurant('Dominos', 'Pizzaria')
restaurant3 = Restaurant('Estancia Grill', 'Churrascaria')
restaurant4 = Icecream('Sergel', 'Sorveteria')

restaurant1.describe_restaurant()
restaurant1.open_restaurant()

restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

restaurant3.read_served()
restaurant3.set_number_served(2)
restaurant3.increment_number_served(3)

restaurant4.describe_restaurant()
restaurant4.describeflavors()
