def dfs(n, lst):
    if n == L:
        cnt = sum(char in 'aeiou' for char in lst)
        cnt2 = sum(i in 'bcdfghjklmnpqrstvwxyz' for i in lst)
        if cnt >= 1:
            if cnt2 >= 2:
                print(*lst)
    for i in range(C):
        if not visited[i]:
            visited[i] = True
            dfs(n+1, lst+[arr[i]])
            visited[i] = False


L, C = map(int, input().split())
arr = list(map(str, input().split()))
arr.sort()
visited = [False] * C
result_lst = []
dfs(0, result_lst)