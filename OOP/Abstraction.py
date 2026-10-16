from abc import ABC, abstractmethod

class Abstract(ABC):

    @abstractmethod
    def Area(self):
        pass

    @abstractmethod
    def Perimeter(self):
        pass


class Square(Abstract):

    def show(self):
        print("Hello")

    def Area(self):
        print("Area of Square...")

    def Perimeter(self):
        print("Perimeter of Square...")


obj = Square()

obj.show()



