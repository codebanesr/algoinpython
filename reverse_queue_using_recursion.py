def reverseq(q):
	if len(q)>1:
		#take out the first element
		x = q.pop(0)
		#reverse the remaining queue
		reverseq(q)
		#add x to the reversed queue and the entire queue is reversed
		q.append(x)

q = [1,2,3,4,5,6]
reverseq(q)
print(q)