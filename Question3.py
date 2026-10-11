# Write a Python function to multiply all the numbers in a list.

def Mul_number(a : list):
    mul = 1
    for i in a:
        mul = mul*i
    return mul

a = [2,5,7,8]

print(Mul_number(a))