def solution(num):
    str_num = str(abs(num))
    return str_num[::-1] if num > 0 else '-{}'.format(str_num[::-1])

print(solution(-231))
print(solution(345))