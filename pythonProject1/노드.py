from collections import deque


def bfs(start, goal, graph, V):
    visited = [False] * (V + 1)
    dist = [0] * (V + 1)

    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        cur = queue.popleft()

        if cur == goal:
            return dist[cur]

        for i in graph[cur]:
            if not visited[i]:
                visited[i] = True
                dist[i] = dist[cur] + 1
                queue.append(i)

    return 0


def solve(test_cases):
    ans = []

    for case in test_cases:
        V, line, S, G = case

        graph = [[] for _ in range(V + 1)]

        for u, v in line:
            graph[u].append(v)
            graph[v].append(u)

        result = bfs(S, G, graph, V)
        ans.append(result)

    return ans


T = int(input())
test_cases = []

for _ in range(T):
    V, E = map(int, input().split())
    line = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    test_cases.append((V, line, S, G))

ans = solve(test_cases)

for i in range(T):
    print(f'#{i + 1}', ans[i])