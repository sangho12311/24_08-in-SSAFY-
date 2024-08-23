from collections import deque

lis = [1, 3, 5, 7, 9]

lis.append(55)
print(lis)



lis_d = deque(lis)
lis_d.appendleft(55)
print(lis_d)
