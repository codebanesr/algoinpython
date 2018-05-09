#!/usr/bin/python3
def msort(l):
	if len(l)<2:
		return l
	mid = len(l)//2
	left = l[:mid]
	right = l[mid:]

	left = msort(left)
	right = msort(right)

	i,j = 0,0
	#clear l now 
	l = []
	while i<len(left) and j<len(right):
		if left[i]<right[j]:
			l.append(left[i])
			i+=1
		else:
			l.append(right[j])
			j+=1
	l = l+left[i:]
	l = l+right[j:]
	return l


arr = [int(x) for x in input().split(" ")]
print(arr)
print(msort(arr))

