a = [1,5,9,10,15,20]
b = [2,3,8,13]
m = len(a)
n = len(b)

def solution(a, b, m, n):
    for i in range(n-1, -1, -1):
        last = a[m-1]
        j = m - 2
        while(j>=0 and a[j] > b[i]):
            a[j+1] = a[j]
            j -= 1
        if(j != m -2 and last > b[i]):
            a[j+1] = b[i]
            b[i] = last







    # for i in range(n-1, -1, -1):
    #     last = a[m-1]
    #     j = m - 2
    #     while(j >=0 and a[j] > b[i]):
    #         a[j+1] =  a[j]
    #         j-= 1

    #     if (j != m-2 or last >b[i]):
    #         a[j+1] = b[i]
    #         b[i] = last





solution(a, b, m, n)

print("After Merging \nFist Array:", end="")
for i in range(m):
    print(a[i], " ", end="")

print("\nSecond Array:", end="")
for i in range(n):
    print(b[i], " ", end="")
