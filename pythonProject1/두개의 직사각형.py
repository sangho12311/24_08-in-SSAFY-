def determine_state(rect1, rect2):
    x1, y1, x2, y2 = rect1
    x3, y3, x4, y4 = rect2

    if x1 < x4 and x2 > x3 and y1 < y4 and y2 > y3:
        return result.append('1')

    if (x2 == x3 or x1 == x4) and (y1 < y4 and y2 > y3):
        return result.append('2')
    if (y2 == y3 or y1 == y4) and (x1 < x4 and x2 > x3):
        return result.append('2')

    if (x2 == x3 and y2 == y3) or (x1 == x4 and y1 == y4) or (x2 == x3 and y1 == y4) or (x1 == x4 and y2 == y3):
        return result.append('3')

    return result.append('4')


result = []
T = int(input())
for t in range(1, T + 1):
    rect1 = list(map(int, input().split()))
    rect2 = list(map(int, input().split()))
    state = determine_state(rect1, rect2)
for i in range(T):
    print(f'#{i + 1}', result[i])