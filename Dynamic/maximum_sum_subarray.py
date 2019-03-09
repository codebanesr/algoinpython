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

















# M-2
arr  = [1,2,-5,6,7,-10,5,6,7,8]
# arr= [1,2,-5,1,0]
sum_till_now, max_sum = 0,0
for i in range(len(arr)):
    if sum_till_now+arr[i]>0:
        sum_till_now = sum_till_now+arr[i]
        if sum_till_now>max_sum:
            max_sum=sum_till_now
    elif sum_till_now+arr[i]<0:
        sum_till_now = 0
print(max_sum)
