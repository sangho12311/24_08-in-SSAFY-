def maze(N, table):
    # 출발지(2)를 찾기
    start_x, start_y = None, None
    for i in range(N):
        for j in range(N):
            if table[i][j] == 2:
                start_x, start_y = i, j
                break
        if start_x is not None:
            break

    # 출발지가 없으면 에러 처리
    if start_x is None or start_y is None:
        return "error"

    # 방문 여부를 기록할 2D 리스트
    visited = [[False] * N for _ in range(N)]
    # 스택 초기화
    stack = [(start_x, start_y)]

    while stack:
        x, y = stack.pop()

        # 목적지(3)에 도착하면 1을 반환
        if table[x][y] == 3:
            return 1

        # 현재 위치를 방문으로 표시
        visited[x][y] = True

        # 상, 하, 좌, 우로 이동 가능한 위치를 검사
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            # 이동할 위치가 미로 범위 내에 있고, 방문하지 않았으며, 벽이 아닌 경우
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and table[nx][ny] != 1:
                stack.append((nx, ny))

    # 스택이 비어도 목적지에 도달하지 못하면 0을 반환
    return 0

# 입력 받기
T = int(input().strip())  # strip() 메서드를 추가하여 입력 값의 불필요한 공백 제거
for tc in range(1, T + 1):
    N = int(input().strip())  # strip() 메서드를 추가하여 입력 값의 불필요한 공백 제거
    table = []
    for _ in range(N):
        table.append(list(map(int, input().strip())))  # 각 줄의 입력을 table에 추가하도록 수정

    result = maze(N, table)
    print(f'#{tc} {result}')
