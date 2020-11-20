def binary_search(arr, key):
    left = 0
    right = len(arr) -1
    matched = False
    if not matched and left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            matched = True
        else:
            if arr[mid] < key:
                left = mid + 1
            else:
                right = mid
    return matched



# def binary_search(lst, key):
#     left = 0
#     right = len(lst) - 1
#     matched = False
#     while (left<=right and not matched):
#         mid = (left + right) // 2
#         if lst[mid] == key:
#             matched = True
#         else:
#             if key < lst[mid]:
#                 right = mid
#             else:
#                 left = mid + 1
#     return matched

print(binary_search([1, 3, 9, 15], 17))
print(binary_search([1, 3, 9, 15], 3))