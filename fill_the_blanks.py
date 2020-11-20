array1=[1,None,2,3,None,None,5,None]

def solution(arr):
    result = []
    temp = 0
    for a in arr:
        if a is not None:
            result.append(a)
            temp = a
        else:
            result.append(temp)

    return result




print(solution(array1))