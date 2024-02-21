from __future__ import annotations

class calculator:
    """calculator class handling addition, multiplication, subtraction, division"""
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
        