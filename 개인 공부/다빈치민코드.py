def dfs(n, s, lst):
    global temp
    if n == M:
        for i in lst:
            temp *= arr[i]
        ans.append(temp)
        temp = 1
    for j in range(s, N):
        dfs(n+1, j+1, lst+[j])

N, M = map(int, input().split())
arr = list(map(int, input().split()))
ans = 9*M
ans_lst = []
temp = 1
dfs(0, 0, [])
print(min(ans))
