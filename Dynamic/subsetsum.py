def subset(arr, sum):
    n = len(arr)+1
    dp = [[True]*(sum+1)]*n

    for i in range(n):
        dp[i][0] = True
    for i in range(1, sum+1):
        dp[0][i] = False


    for i in range(1, n):
        for j in range(1, sum+1):

            if j>=arr[i-1]:
                dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[len(arr)][sum]



sset = [1,2,3]
sum = 7

if (subset(sset, sum)):
    print("Found a subset with the given sum")


else:
    print("Couldnot find a subset with the given sum")







# recursive solution
# def isSubsetSum(set,n, sum) :
   
#     # Base Cases
#     if (sum == 0) :
#         return True
#     if (n == 0 and sum != 0) :
#         return False
  
#     # If last element is greater than
#     # sum, then ignore it
#     if (set[n - 1] > sum) :
#         return isSubsetSum(set, n - 1, sum);
  
#     # else, check if sum can be obtained
#     # by any of the following
#     # (a) including the last element
#     # (b) excluding the last element   
#     return isSubsetSum(set, n-1, sum) or isSubsetSum(set, n-1, sum-set[n-1]