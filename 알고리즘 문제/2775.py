T=int(input())
for tc in range(T):
    k=int(input())
    n=int(input())
    apart=[[0]*(n+1) for _ in range(k+1) ]
    for i in range(1,n+1): #i는 호 
        apart[0][i]=i
    for i in range(1,k+1):
        for j in range(1,n+1):#j는 층수
            apart[i][j]=apart[i-1][j]+apart[i][j-1]
    print(apart[k][n])