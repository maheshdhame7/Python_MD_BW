# Write a Python function that accepts a string and counts the number of upper and lower case letters.

def count_latters(a : str):
    upper = 0
    lower = 0

    for ch in a:
        if ord(ch)>=65 and ord(ch)<=90:
            upper = upper +1
        elif ord(ch)>=97 and ord(ch)<=122:
            lower = lower + 1

    return [upper,lower]

a = """I am Mahesh Dhame"""

result = count_latters(a)

print("Upper :",result[0])
print("Lower : ",result[1])