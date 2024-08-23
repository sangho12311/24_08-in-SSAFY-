from collections import deque

n= int(input())
MAP =[list(map(int, input().split())) for _ in range(n)]

def bfs(node):
    q = deque([node])
    visited = [0] * n
    visited[node] = 1

    while q:
        now = q.popleft()
        print(now, end = ' ')
        for i in range(n):
            # 이미 방문했거나 (visited 배열이 1), 연결되어 있지 않은 노드 (인접 행렬이 0)이면 continue
            if MAP[now][i] == 0 or visited[i] == 1:
                continue
            visited[i] =1
            q.append(i)
bfs(0)