num1 = '364'
num2 = '1836'
def string_to_int(num):
    int_num = 0
    for idx, n in enumerate(num):
        int_num += (ord(n) - ord("0")) * 10 ** (len(num)-idx-1)
    return int_num

def solution(num1, num2):
    return string_to_int(num1) + string_to_int(num2)

print(solution(num1, num2))