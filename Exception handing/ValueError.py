def Add_two_number(a , b : int):
    c = a+b
    return c  

try:
    a, b = map(int, input("Enter two numbers: ").split())
     
    print(Add_two_number(a,b))

except ValueError:
    print("Exception occurred: Please enter two valid integers.")
except Exception as e:
    print(f"Exception occure : {e}")

print("hello")

