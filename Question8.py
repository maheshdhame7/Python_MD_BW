# Write a Python function that checks whether a passed string is a palindrome or not.

def Is_palindrome(a : str):
    rev = ""
    for ch in a:
        rev = ch + rev
    if rev == a:
        return "string is palindrome..."

a = 'amamma'

print(Is_palindrome(a))