def minmax(arr):
    minimum=arr[0]
    maximum = arr[0]
    if len(arr) == 1:
        return {"minimum":arr[0], "maximum":arr[0]}
    elif  len(arr)==2:
        minimum, maximum = min(arr[0], arr[1]), max(arr[0], arr[1])
        return {"minimum":minimum, "maximum":maximum}
    else:
        mid = len(arr)//2
        left = minmax(arr[:mid])
        right = minmax(arr[mid:])
        maximum = left["maximum"] if left["maximum"]>right["maximum"] else right["maximum"]
        minimum = left["minimum"] if right["minimum"]>left["minimum"] else right["minimum"]
    return {"maximum":maximum, "minimum":minimum}



arr = [10,2,3,4,5,6,7,8]
print(minmax(arr))


