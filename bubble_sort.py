def bubble_sort(lst):
    iter_len = (len(lst) -1)
    for i in range(iter_len):
        for j in range(iter_len - i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

lst = [15, 1, 9, 3]
print(bubble_sort(lst))

