def lin_search(lst, key):
    for i in range(len(lst)):
        if lst[i] == key:
            return i
    return 'Not found'


lst = [15, 1, 9, 3]

print(lin_search(lst, 1))


