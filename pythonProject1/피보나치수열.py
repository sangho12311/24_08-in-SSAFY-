n=int(input())

lst=[0]*(n+1)
lst[0] = 0
lst[1] = 1
def fibo(n):
    if n>=2 and lst[n]==0:
        lst[n] = fibo(n-1)+fibo(n-2)
    return lst[n]

print(fibo(n-1))
