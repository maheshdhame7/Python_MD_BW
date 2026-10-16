class Factory:
    __a = 1000
    def __init__(self,material,zips,pockets):
        self.material = material
        self.zips = zips
        self.pockets = pockets
        self.a = Factory.__a
        Factory.__a = Factory.__a + 1
        
    def Display(self):
        print(f"Material : {self.material} Total zips : {self.zips} Total pockets : {self.pockets}, a : {self.__a},class a: {Factory.__a}")
obj = Factory("Leather",3,5)
obj.Display()
obj2 = Factory("Leather",3,5)
obj3 = Factory("Leaeerere",3,5)
obj2.Display()

obj.Display()
obj3.Display()
A=25

A = A+1

print(A)

# print(obj.pockets)


