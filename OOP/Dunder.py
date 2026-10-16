class Animal:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"name : {self.name}"

    def __add__(self, other):
        return f"ages : {self.age + other.age}"

obj = Animal("Dog",12)
obj2 = Animal("Cat",2)
print(obj)

print(obj + obj2)