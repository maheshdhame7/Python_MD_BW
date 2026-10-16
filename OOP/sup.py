class Animal:
    def __init__(self,name):
        self.name = name

    def show(self):
        print(f"Name : {self.name}")

class Person(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def show(self):
        print(f"Name : {self.name},Age : {self.age}")


obj = Animal("Mahesh")
obj.show()

obj1 = Person("Tejas",25)
obj1.show()