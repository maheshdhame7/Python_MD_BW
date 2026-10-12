

a = int(input("Enter tha number : "))

try:
    print(10/a)

except Exception as e:
    print(f"Exception occure : {e}")

else:
    print("there is no exception occure...")

finally:
    print("alway run...")


print("Work done...")