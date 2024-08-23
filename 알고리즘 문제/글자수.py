T=int(input())

for tc in range(1,T+1):
    str1=list(input())
    str2=list(input())
    include_lst=[]
    for i in str1:
        sum=0
        for j in str2:
            if j==i:
                sum+=1
        include_lst.append(sum)
    print(f'#{tc} {max(include_lst)}')
        
        