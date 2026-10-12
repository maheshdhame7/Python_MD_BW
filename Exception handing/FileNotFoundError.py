
def Open_file():
    with open('D:/Mahesh Dhame/Machine learning/Python Folder/Exception handing/ValueErrork.py','r') as f:
        print(f.read())
        f.close()

try:
    Open_file()

except FileNotFoundError:
    print("File not found")

print("Hello world")

