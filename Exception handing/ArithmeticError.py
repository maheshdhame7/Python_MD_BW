try:
    a = 10/0
    print(a)
except ArithmeticError:
    print("Cant divide by zero...")

print("Hello wolrd")