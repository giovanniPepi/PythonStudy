
class Restaurant:
    """Places you can eat"""

    def __init__(self, name, type):
        self.name = name
        self.type = type
    
    def describe_restaurant(self):
        """Gives information about places human can eat"""
        print(f"This restaurant is called {self.name} and is of the {self.type} kind.")
    
    def open_restaurant(self):
        """Warns humans that the place is open"""
        print(f"{self.name} is now open.")

restaurant1 = Restaurant('Olive Garden', 'Italian')
restaurant2 = Restaurant('Dominos', 'Pizzaria')
restaurant3 = Restaurant('Estancia Grill', 'Churrascaria')

restaurant1.describe_restaurant()
restaurant1.open_restaurant()

restaurant2.describe_restaurant()
restaurant3.describe_restaurant()



