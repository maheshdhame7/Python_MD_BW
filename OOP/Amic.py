class Animal:

    name = "Tommy"

    def __init__(self,age):
        self.age = age

    def show(self):
        print(f"Animal age : {self.age}")

    @classmethod
    def hello(cls):
        print("Hello your name is.")

    @staticmethod
    def stat():
        print("This is static method")



obj = Animal(12)

obj.show()
obj.hello()
obj.stat()