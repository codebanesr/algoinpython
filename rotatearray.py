#!/usr/bin/python3

def rotatearr(arr, by):
	arr = arr[by:]+arr[:by]
	return arr
	

arr = [1,2,3,4,5,6]
print(rotatearr(arr, 3))


