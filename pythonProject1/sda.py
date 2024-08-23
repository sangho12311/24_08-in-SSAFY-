def check(arr):
    stack = []
    for i in arr[:-1]:  # 마지막 "." 제외하고 순회
        if i.isdecimal():
            stack.append(int(i))
        elif i in {'+', '-', '*', '/'}:
            if len(stack) < 2:  # 스택에 숫자가 2개 미만이면 return 에러
                return 'error'
            b = stack.pop()  # 두 번째 숫자
            a = stack.pop()
            if i == '+':
                stack.append(a + b)
            elif i == '-':
                stack.append(a - b)
            elif i == '*':
                stack.append(a * b)
            elif i == '/':
                stack.append(a // b)
    if len(stack) != 1:
        return 'error'

    return stack[0]  # 최종 결과 반환


T = int(input())
for tc in range(1, T + 1):
    F = input().split()
    result = check(F)
    print(f'#{tc} {result}')