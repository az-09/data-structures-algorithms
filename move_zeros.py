array1=[0,1,0,3,12]
array2=[1,7,0,0,8,0,10,12,0,4]

def solution(nums):
    for num in nums:
        if num == 0:
            nums.remove(0)
            nums.append(num)
    return nums

print(solution(array1))
print(solution(array2))