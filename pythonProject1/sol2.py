N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
K = int(input())


max_monsters = 0
directions = [(-1, -1), (-1, 1), (1, 1), (1, -1)]

for i in range(N) :
    for j in range(N) :
        total = 0
        for dx, dy in directions :
            for step in range(1, K + 1) :
                nx = i + dx * step
                ny = j + dy * step
                if 0 <= nx < N and 0 <= ny < N :
                    total += grid[nx][ny]
            if max_monsters < total :
                max_monsters = total
print(max_monsters)