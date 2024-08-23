def forth(arr):
    cod_lst=arr.split()
    stack=[]
    if '.' not in cod_lst:
        return 'error'
    for cod in cod_lst:
        if cod.isdigit():
            stack.append(cod)
        elif cod in ['+','-','*','/']:
            b = int(stack.pop())
            a = int(stack.pop())
            if cod == '+':
                stack.append(a + b)
            elif cod == '-':
                stack.append(a - b)
            elif cod == '*':
                stack.append(a * b)
            elif cod == '/':
                stack.append(a // b)




