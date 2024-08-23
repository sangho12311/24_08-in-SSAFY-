from itertools import combinations

N,M=map(int,input().split())

arr=list(map(int,input().split()))
sum_lst=[]
tsum_lst=[]
for combs in (combinations(arr,3)):
    temp_sum=sum(combs)
    sum_lst.append(temp_sum)

for i in sum_lst:
    tsum_lst.append(i-M)

print(min(tsum_lst)+M)




