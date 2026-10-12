a = [1,2,3]

try:
    p = a[3]+2
    print(p)
except IndexError:
    print("Intex not found...")