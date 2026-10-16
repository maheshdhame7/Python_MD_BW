# Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically

def sort_line(a : str):

    r = a.split('-')
    r.sort()
    result = "-".join(r)

    return result

a = "abc-pkl-opi"

print(sort_line(a))