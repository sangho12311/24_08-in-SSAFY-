def re__text(text):
    stack=[]

    for i in text:
        if stack and i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)

    return stack

T=int(input())
for tc in range(1,T+1):
    text=input()
    print(f'#{tc} {len(re__text(text))}')
