def lis(arr):
    dp = [1]*len(arr)   #there is always a subsequence with length of 1
    for i in range(len(arr)):
        for j in range(i):
            dp[i] = max(dp[j]+1, dp[i]) if arr[j] < arr[i] else dp[i]   #if some element does not satisfy the rule
                                                                        #just ignore it and carry the previous result
    return dp

arr = [5,4,1,6,11,9,10]
result = lis(arr)
print(arr)
print(result)
