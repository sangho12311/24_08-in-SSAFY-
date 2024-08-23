N, M, V = map(int,input().split())

for i in range(M):
  x, y = map(int, input().split())
  table[x][y] = 1
  table[y][x] = 1

visited1 = [False] * (N+1)
visited2 = [False] * (N+1)

def dfs(V):
  visited1[V] = True
  print(V, end= " ")
  for i in range(1, N+1):
    if not visited1[i] and graph[V][i] == 1:
      dfs(i)

dfs(V)
