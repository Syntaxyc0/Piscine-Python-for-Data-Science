from S1E9 import Character

class Baratheon(Character):
    """Class representing the Baratheon family inherited from the character one"""
    def __init__(self, first_name: str, is_alive: bool = True):
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"
    
    def die(self):
         """Method to declare death of a Baratheon element"""
         self.is_alive = False
        
    def __str__(self) -> str:
        return f"Vector: ('{self.__class__.__name__}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self) -> str:
        return f"Vector: ('{self.__class__.__name__}', '{self.eyes}', '{self.hairs}')"
    
    def create_baratheon(first_name: str, is_alive: bool = True):
        return Baratheon(first_name, is_alive)
 
         
class Lannister(Character):
    """Class representing the Lannister family inherited from the character one"""
    def __init__(self, first_name: str, is_alive: bool = True):
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"
    
    def die(self):
         """Method to declare death of a Lannister element"""
         self.is_alive = False
        
    def __str__(self) -> str:
        return f"Vector:  ('{self.__class__.__name__}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self) -> str:
        return f"Vector: ('{self.__class__.__name__}', '{self.eyes}', '{self.hairs}')"
    
    def create_lannister(first_name: str, is_alive: bool = True):
        return Lannister(first_name, is_alive)