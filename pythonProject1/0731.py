# 방향 배열 : 2차원 맵(배열)에서 현재 위치를 기준으로 이동할 수 있는 방향을 나타내는 배열
# dy = [-1, 1, 0, 0] # 상 하 좌 우
# dx = [0, 0, -1 ,1] # 상 하 좌 우

# dy = [-1, -1, 1, 1]
# dx = [-1, 1, -1, 1]

# 사용법 : 현재 위치 (y,x) i번째 방향으로 이동
# ---> ny, nx = y + dy[i], x + dx[i]
for i in range(4) : # 방향이 4방향
    ny, nx = y + dy[i], x + dx[i]

for dy, dx in direcitons : # ex) 방향 튜플 4방향
    ny, nx = y + dy, x + dx

# 방법 2 (continue 사용)

arr = [['_'] * 5 for _ in range(4)]
for _ in range(2) :
    y, x = map(int, input().split())
    # di, dj // dr, dc
    dy = [-1, -1, -1, 0, 1, 1, 1, 0]
    dx = [-1, 0, 1, 1, 1, 0, -1, -1]
    for i in range(8) : # 8가지 방향
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < 4 and 0 <= nx < 5 :
            arr[ny][nx] = '#'

for row in arr :
    print(*row)

# 방법3 (방향 튜플 사용)
arr = [['_'] * 5 for _ in range(4)]
directions = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, 0), (1, -1), (1, 1)]

for _ in range(2) :
    y, x = map(int, input().split())
    for dy, dx in directions :
        ny, nx = y + dy, x + dx
        if 0 <= ny < 4 and 0 <= nx < 5 :
            arr[ny][nx] = '#'

for row in arr :
    print(*row)