from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int,input().split()))
    q = deque(lst)
    q.rotate(N-M)
    print(f'#{tc} {q[0]}')

