def merge_sort(lst, left, right):
    if right - left > 1:
        mid = (left + right) // 2
        merge_sort(lst, left, mid)
        merge_sort(lst, mid, right)
        merge_list(lst, left, mid, right)

def merge_list(lst, left, mid, right):
    left_list = lst[left:mid]
    right_list = lst[mid:right]
    k = left
    i = 0
    j = 0
    while(left +i < mid and mid+j < right):
        if(left_list[i] <= right_list[j]):
            lst[k] = left_list[i]
            i += 1
        else:
            lst[k] = right_list[j]
            j += 1
        k += 1
    if left + i < mid:
        lst[k] = left_list[i]
        i += 1
        k += 1
    else:
        while k < right:
            lst[k] = right_list[j]
            j += 1
            k += 1

our_list = input('input - unordered elements:').split()
our_list = [int(x) for x in our_list]
merge_sort(our_list, 0, len(our_list))
print(our_list)
