def postord(n):
    if n<=N:
        if lst[n] == 0:
            lst[n] = postord(n*2) + postord(n*2+1)
        return lst[n]
    else:
        return 0


T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    lst = [0] * (N+1)
    for _ in range(M):
        idx, v = map(int, input().split())
        lst[idx] = v

    ans = postord(L)
    print(f'#{tc} {ans}')
