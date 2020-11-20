# Runtime complexity: Liner, O(N) O(N)
# Memory complexity: Constant, O(1) O(1)

def move_zeros_to_left(arr):
    if len(arr) < 1:
        return

    read_idx = len(arr) - 1
    write_idx = len(arr) - 1

    while read_idx >=0:
        if arr[read_idx] != 0:
            arr[write_idx] = arr[read_idx]
            write_idx -= 1
        read_idx -=1

    while write_idx >= 0:
        arr[write_idx] = 0
        write_idx -= 1




# def move_zeros_to_left(arr):
#     if len(arr) < 1:
#         return

#     read_idx = len(arr) - 1
#     write_idx = len(arr) - 1

#     while read_idx >= 0:
#         if arr[read_idx] != 0:
#             arr[write_idx] = arr[read_idx]
#             write_idx -=1
#         read_idx -=1

#     while write_idx >= 0:
#         arr[write_idx] = 0
#         write_idx -= 1

v = [1,10,20,0,59,63,0,88,0]
print('original array', v)
move_zeros_to_left(v)
print('after moving zeros to left',v)