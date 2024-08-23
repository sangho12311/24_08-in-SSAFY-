def cola(N,i):
    if N==1:
        return i

    elif N%2==0:
        return cola(N//2,i+1)


    else:
        return cola((3*N)+1,i+1)

N=int(input())
print(cola(N,0))