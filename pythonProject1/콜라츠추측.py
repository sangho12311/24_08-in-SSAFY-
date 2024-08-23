def cola(N,i):
    if N==1:
        return i

    elif N%2==0:
        i+=1
        cola(N//2)

    else:
        i+=1
        cola((3*N)+1)

N=int(input())
print(cola(N,1))