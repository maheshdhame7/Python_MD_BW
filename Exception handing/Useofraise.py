age = int(input("Enter the age :"))

try:
    if age <18:
        raise ValueError("You are not eligible for voting.")
    else:
        print("Welcome to voting center...")

except Exception as e:
    print(f"Exception occure as : {e}")

print("Thank you...")