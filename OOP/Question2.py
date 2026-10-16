# 2. Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.

from datetime import date


class Person:
    def __init__(self,name,country,dob : date):
        self.name = name
        self.country = country
        self.dob = dob

    def Find_age(self):
        curr = date.today()
        return curr.year - self.dob.year

obj = Person(
"Mahesh",
"India",
date(2002, 5, 15)  # Example date of birth
)

print(obj.Find_age())