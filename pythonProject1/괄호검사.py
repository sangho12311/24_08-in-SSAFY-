def bracket(text):
    stack=[]
    open_bracket='({['
    close_bracket=')}]'
    ans=0
    for char in text:
        if char in open_bracket:
            stack.append(char)
            ans+=1
        elif stack[-1] in open_bracket and char in close_bracket:
                if not stack:
                    return False
                elif stack[-1]=='(' and char==')':
                    stack.pop()
                    ans -= 1
                elif stack[-1]=='{' and char=='}':
                    stack.pop()
                    ans -= 1
                elif stack[-1]=='[' and char==']':
                    stack.pop()
                    ans -= 1


    if ans!=0:
        ans=0
    else:
        ans=1
    return(ans)

T=int(input())

for tc in range(1,T+1):
    text=input()
    result=bracket(text)
    print(f'#{tc} {result}')


