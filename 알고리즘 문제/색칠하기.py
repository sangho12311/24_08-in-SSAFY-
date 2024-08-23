T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    red_lst = []
    blue_lst = []
    result = 0
    for _ in range(N):
        y1, x1, y2, x2, color = map(int, input().split())

        for i in range(y1, y2 + 1):
            for j in range(x1, x2 + 1):
                if color == 1:
                    red_lst.append([i, j])
                if color == 2:
                    blue_lst.append([i, j])
    # 각 리스트를 비교해서 공통인적인 좌표들만 카운트
    for common in red_lst:
        result += blue_lst.count(common)

    print(f'#{tc} {result}')