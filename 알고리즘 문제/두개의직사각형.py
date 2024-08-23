T=int(input())

for tc in range(1,T+1):
    R1x1,R1y1,R1x2,R1y2=map(int,input().split())
    # R2x1,R2y1,R2x2,R2y2=map(int,input().split())
    table = [[0]*1000 for i in range(1000)]
    for r1 in range(R1y1,R1y2):
        for c1 in range(R1x1,R1x2):
            table[r1][c1]+=1
    # for r2 in range(R2y1,R2y2):
    #     for c2 in range(R2x1,R2x2):
    #         table[r2][c2]+=1  
    # print(table)
    # if 2 in table:
    #     for r in range(1000):
    #         for c in range(1000):
    #             if table[r][c] == 2:
    #                 if table[r+1][c+1] == 2:
    #                     result = 1 
    #                     break
    #                 elif table[r+1][c] == 2 or table[r][c+1] == 2:
    #                     result = 2
    #                     break
    #                 else:
    #                     result = 3
    #                     break
    # else:
    #     result = 4
    # print(result)

