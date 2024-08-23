R,C=map(int,input().split())

table=[[False for _ in range(C)] for _ in range(R)]
ANS=0

r,c,i,cnt=[0,0,0,1]
D=[(0,1),(1,0),(0,-1),(-1,0)]

while R*C > cnt:
    table[r][c]=True
    nr,nc=(r+D[i][0],c+D[i][1])
    if nr>=R or nr<0 or nc>=C or nc<0 or table[nr][nc]:
        i=(i + 1)%4
        ANS+=1
    else:
        r,c=(nr,nc)
        cnt+=1
print(ANS)