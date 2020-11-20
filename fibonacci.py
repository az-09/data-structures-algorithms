def Fibanacci1(n):
    if n < 0:
        return
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    else:
        return Fibanacci1(n-1) + Fibanacci1(n-2)

def Fibanacci2(n):
    a = 0
    b = 1
    if n < 0:
        return
    elif n == 1:
        return a
    elif n == 2:
        return b
    else:
        for i in range(2, n):
            c = a + b
            a, b = b, c
        return b



print(Fibanacci2(9))
# assert Fibanacci1(150) != Fibanacci2(150)