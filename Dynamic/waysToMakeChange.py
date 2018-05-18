def makechange(arr, change):
    dp = [0]*(change+1)
    dp[0] = 1   #there is always 1 way to make a change for 0 ; Dont take anything
    for coin in arr:
        for j in range(1, change+1):
            if j>=coin:     #never forget that equals to
                dp[j] += dp[j-coin] #whatever you have calculated with other coins + whatever you may get with this coin

    return dp

a =[2,5,3,6]
change = 10
print(makechange(a, change))