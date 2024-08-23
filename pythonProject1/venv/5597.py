lst = [0]*30

for i in range(28):
    N = int(input())
    lst[N-1] = 1

for i in range(30):
    if lst[i] == 0:
        print(i+1)
