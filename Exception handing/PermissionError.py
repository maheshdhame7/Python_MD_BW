def Write_file():
    with open("D:/Mahesh Dhame/oop-Assignment.txt",'a') as f:
        f.append("Helo")
        f.close()

try:
    Write_file()
except PermissionError:
    print("You have not permission to write in it")