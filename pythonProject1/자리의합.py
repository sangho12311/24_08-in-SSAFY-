
def suming(N):
    if N<10:
        return N
    else:
        return suming(N//10)+N%10

N=int(input())
print(suming(N))