def Addition(a: int, b: int):
    if not isinstance(a,int) or not isinstance(b,int):
        raise TypeError("Input has an invalid type.")
    return a + b

try:
    b = input("Enter two numbers: ")
    print("Sum:", Addition('20',b))



except Exception as e:
    print(e)