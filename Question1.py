# 1. Write a Python function to find the maximum of three numbers.

def find_max(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c

a = 10
b = 20
c= 30

print(find_max(a,b,c))