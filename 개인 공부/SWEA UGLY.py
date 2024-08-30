lst = [1]
for i in range(2, 10001):
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
        lst.append(i)
Q = int(input())
ans_lst = list(map(int, input().split()))
for j in ans_lst:
    print(lst[j-1], end = " ")
