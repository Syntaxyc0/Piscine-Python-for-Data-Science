from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """King class that inherits from the Baratheon and the Lannister one"""
    def __init__(self, first_name: str, is_alive: bool = True):
        Lannister.__init__(self, first_name, is_alive)
        Baratheon.__init__(self, first_name, is_alive)
        
    def get_eyes(self):
        """Get eye color"""
        return self.eyes
    
    def get_hairs(self):
        """Get hair color"""
        return self.hairs
    
    def set_eyes(self, eyes: str):
        """Sets eye color"""
        self.eyes = eyes
        
    def set_hairs(self, hairs: str):
        """Sets hair color"""
        self.hairs = hairs