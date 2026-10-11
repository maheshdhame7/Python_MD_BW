# 10. Write a Python program to detect the number of local variables declared in a function.


def example():
    a = 10
    b = 20
    c = 30
    d = "hello"

    print("Number of local variables:", len(locals()))

example()