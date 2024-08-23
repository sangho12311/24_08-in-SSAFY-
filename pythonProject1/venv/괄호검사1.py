def bracket(text):
    stack=[]
    open_bracket='({['
    close_bracket=')}]'
    ans=0
    for char in text:
        if char in open_bracket:
            stack.append(char)

        elif char in close_bracket:
            if stack==[]:
                ans=0
                return  ans

            if stack[-1]=='(' and char==')':
                stack.pop()

            elif stack[-1]=='{' and char=='}':
                stack.pop()

            elif stack[-1]=='[' and char==']':
                stack.pop()
            else:
                return 0

    if stack==[]:
        ans=1
    else:
        ans=0
    return  ans

T=int(input())

for tc in range(1,T+1):
    text=input()
    result=bracket(text)
    print(f'#{tc} {result}')


