T = int(input())
for tc in range(1, T+1):
    N = int(input())
    stop = [0]*5001
    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A, B+1):
            stop[i] += 1
    P = int(input())
    v = []
    for j in range(P):
        C = int(input())
        num = stop[C]
        v.append(num)
    print(f'#{tc} {" " .join(map(str,v))}')
