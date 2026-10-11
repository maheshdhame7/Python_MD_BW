# Write a Python function to check whether a number falls within a given range.

def bet_range(a,min,max):
    if a>min and a<max :
        return "between the range.."
    else:
        return "Not in range..."

a = 10
b = 5
c = 52


print(bet_range(a,b,c))