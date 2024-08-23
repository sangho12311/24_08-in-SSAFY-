def rock(N, r, c, arr):
    cnt = 0
    for i in range(5):  # 가로 방향으로 검사
        if c + 4 < N:  # 가로 방향에서 c+4까지 검사
            if arr[r][c + i] == 'o':  # arr[r][c+i]로 인덱스 수정
                cnt += 1
            else:
                break
    if cnt == 5:
        return 'YES'

    cnt = 0
    for j in range(5):  # 세로 방향으로 검사
        if r + 4 < N:  # 세로 방향에서 r+4까지 검사
            if arr[r + j][c] == 'o':  # arr[r+j][c]로 인덱스 수정
                cnt += 1
            else:
                break
    if cnt == 5:
        return 'YES'

    cnt = 0
    for k in range(5):  # 오른쪽 아래 대각선 검사
        if r + 4 < N and c + 4 < N:  # r+4와 c+4가 범위를 벗어나지 않게 설정
            if arr[r + k][c + k] == 'o':
                cnt += 1
            else:
                break
    if cnt == 5:
        return 'YES'

    cnt = 0
    for l in range(5):  # 왼쪽 아래 대각선 검사
        if r + 4 < N and c - 4 >= 0:  # c-4가 0 이상이 되도록 설정
            if arr[r + l][c - l] == 'o':
                cnt += 1
            else:
                break
    if cnt == 5:
        return 'YES'

    return 'NO'

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(str(input())) for _ in range(N)]
    found = False  # 결과를 찾았는지 확인
    for i in range(N):
        for j in range(N):
            if rock(N, i, j, arr) == 'YES':
                print(f'#{tc} YES')
                found = True
                break
        if found:  # YES가 출력된 후 외부 루프 중단
            break
    if not found:
        print(f'#{tc} NO')
