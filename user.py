class User:

    def __init__(self, first_name, last_name, age, interests):
        """Stores DATA about user"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.interests = interests
    
    def describe_user(self):
        """Describres USER"""
        print(f"Hello, {self.first_name} {self.last_name}!")
        print(f"Your age is {self.age} and your interests are {self.interests}.")

class Privileges:

    def __init__(self):        
        privileges = ['can add posts', 'can delete posts', 'can ban users', 'can lock threads']
    
    def show_privileges(self):
        privileges = ['can add posts', 'can delete posts', 'can ban users', 'can lock threads']
        for privilege in privileges:
            print(f"You {privilege} (9-8 exercise)")   


