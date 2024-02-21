from __future__ import annotations

class calculator:
    """
    calculator class handling addition, multiplication, subtraction, division
    and 3 static methods to realize operations on vectors, dot product, add and substract
    """
    def __init__(self, array: list[int]) -> None:
        self.args = array

    def __add__(self, object) -> None:
        for i in range(len(self.args)):
            self.args[i] += object
        print(*self.args)
        
        
    def __mul__(self, object) -> None:
        for i in range(len(self.args)):
            self.args[i] *= object
        print(*self.args)
        
        
    def __sub__(self, object) -> None:
        for i in range(len(self.args)):
            self.args[i] -= object
        print(*self.args)
        
        
    def __truediv__(self, object) -> None:
        if (object == 0):
            raise ZeroDivisionError
        for i in range(len(self.args)):
            self.args[i] /= object
        print(*self.args)
    
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        res = 0
        for i in range(len(V1)):
            res += V1[i] * V2[i]
        print(f"Dot product is: {res}")
    
    
    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        res = list(range(len(V1)))
        for i in range(len(V1)):
            res[i] = float(V1[i] + V2[i])
        print(f"Add Vector is : {res}")
        
    
    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        res = list(range(len(V1)))
        for i in range(len(V1)):
            res[i] = float(V1[i] - V2[i])
        print(f"Sous Vector is : {res}")
        