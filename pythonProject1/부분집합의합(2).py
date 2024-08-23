def subset(arr,N,K):
    arr = [1,2,3,4,5,6,7,8,9,10,11,12]
    count = 0
    for tar in range(1, 1 << 12):
        sub_sum = 0
        sub_count = 0
        for i in range(12):
            if tar & 0x1:
                sub_sum += arr[i]
                sub_count +=1
            tar >>= 1
        if sub_count == N and sub_sum == k:
            count +=1
    return count






