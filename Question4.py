# Write a Python function to reverse a string.

def rev_string(a : str):
    rev = ""

    for ch in a:
        rev = ch + rev

    return rev

a = "jgf"

print(rev_string(a))