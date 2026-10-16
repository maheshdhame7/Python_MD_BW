class Father:
    def __init__(self,name):
         self.name = name

    def Read(self):
        print("F Can read...")

class Mother:
    def __init__(self,name,age):
         self.name = name
         self.age = age

    def Cook(self):
        print("Can cook..")
    def Read(self):
            print("M Can read...")

class Son(Mother,Father):
    
    def play(self):
        print("Can play..")


obj = Son()
obj.play()
obj.Cook()
obj.Read()

print(Son.mro())