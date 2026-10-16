# 1. Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.

class Circle:
    def __init__(self,redii):
        self.redii = redii

    def Area(self):
        return 2*3.14*self.redii*self.redii

    def Perimeter(self):
        return 2*3.14*self.redii


obj = Circle(5)

print(obj.Area())
print(obj.Perimeter())
        