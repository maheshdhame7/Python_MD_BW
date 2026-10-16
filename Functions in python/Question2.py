# 2. Write a Python function to sum all the numbers in a list.

def Sum_Number(a : list):
    sum = 0
    for i in a:
        sum = sum + i

    return sum

a = [10,5,6,7]

print(Sum_Number(a))