def TOH(n, A, C, B):
	if n>0:
		TOH(n-1, A,B,C)
		print("Move a disk from", A, "to", B ," using", C)
		TOH(n-1, B,C,A)




print("No of disks")
n = int(input())
TOH(n, "A","B","C")