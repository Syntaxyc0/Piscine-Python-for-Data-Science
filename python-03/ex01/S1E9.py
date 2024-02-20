from abc import ABC, abstractmethod


class Character(ABC):
    """An abstract class to define a character"""
    def __init__(self, first_name: str, is_alive: bool = True):
       """Constructor requiring a first name and optionnaly a health status, default one is alive"""
       self.first_name = first_name
       self.is_alive = is_alive
     
    @abstractmethod
    def die(self):
      self.is_alive = False
 
 
class Stark(Character):
	"""Class inherited from the character one"""
	def die(self):
         """Method to declare death of a Stark element"""
         self.is_alive = False