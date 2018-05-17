def lis(arr):
    dp = [0]*len(arr)
    dp[0] = arr[0] if arr[0]>0 else 0
    for i in range(1, len(arr)):
        if arr[i]+dp[i-1]>0:
            dp[i] = dp[i-1]+arr[i]
        # else:
        #     dp[i]=0
        # else statement is not required because in case a negative value is reached that index of the array will not 
        # be updated and it stays 0 *line4*

    return dp


a = [1,2,3,4,5,-20,1,2,5,7,9]
m = lis(a)
print(m)