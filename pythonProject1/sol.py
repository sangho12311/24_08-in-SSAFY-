def bomb_position(N, M ,K, grid) :
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for i in range(N) :
        for j in range(M) :
            if grid[i][j] == '@' :
                for dx, dy in directions :
                    for power in range(1, K + 1) :
                        nx, ny = i + dx * power, j + dy * power
                        if 0 <= nx < N and 0 <= ny < M :
                            if grid[nx][ny] != '#' and grid[nx][ny] != '@':
                                grid[nx][ny] = '%'
                            if grid[nx][ny] == '#' :
                                break
                grid[i][j] = '%'

    return grid
print(17 / 6)
N, M = map(int, input().split())
K = int(input())
grid = [list(input()) for _ in range(N)]

answer = bomb_position(N, M, K, grid)
for row in answer :
    print(''.join(row))