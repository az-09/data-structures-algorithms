def power_rec(x, n):
    if n == 0:
        return 1

    if n == 1:
        return x

    temp = power_rec(x, n//2)
    if n % 2 ==0:
        return temp*temp
    else:
        return x*temp*temp


def power(x, n):
    is_negative = False
    if n < 0:
        is_negative = True
        n *= -1
    result = power_rec(x, n)

    return 1/result if is_negative else result

print(power(2,-2))

assert power(2,-2) == 0.25