N, M = map(int, input().split())

arr = [input().strip() for _ in range(N)]
min_repaints = float('inf')

for x in range(N - 7):
    for y in range(M - 7):
        count_A = 0
        count_B = 0
        num = 0
        for i in range(x, x + 8):
            num += 1
            for j in range(y, y + 8):
                expected_A = 'B' if ((i + j) % 2 == 0) else 'W'
                expected_B = 'W' if ((i + j) % 2 == 0) else 'B'
                if arr[i][j] != expected_A:
                    count_A += 1
                if arr[i][j] != expected_B:
                    count_B += 1
        min_repaints = min(min_repaints, count_A, count_B)

print(min_repaints)
