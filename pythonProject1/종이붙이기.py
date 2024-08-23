from math import factorial

for tc in range(1, int(input())+1):
    n = int(input()) // 10
    arr = [1] * n
    value = 1

    for i in range(n//2):
        arr[i] += arr.pop()
        cnt1 = arr.count(1)
        cnt2 = arr.count(2)

        x = factorial(len(arr)) // factorial(cnt1) // factorial(cnt2)
        value += (2 ** cnt2) * x

    print(f"#{tc} {value}")