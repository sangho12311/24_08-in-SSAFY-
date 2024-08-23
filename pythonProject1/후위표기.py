sentence = list(input())
ans = []
stack = []
for i in sentence:
    if i.isalpha():
        ans.append(i)
    else:
        if i == '(':
            stack.append(i)
        elif i == '*' or i == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                ans.append(stack.pop())
            stack.append(i)
        elif i == '+' or i == '-':
            while stack and stack[-1] != '(':
                ans.append(stack.pop())
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                ans.append(stack.pop())
            stack.pop()
while stack:
    ans.append(stack.pop())

print(''.join(map(str,ans)))