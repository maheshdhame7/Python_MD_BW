# 7. Write a Python function that takes a list and returns a new list with distinct elements from the first list.

def find_dist(a : list):
    r = []
    for n in a:
        if n not in r:
            r.append(n)
    return r


a = [1,4,5,4,5,4,5,4]

print(find_dist(a))