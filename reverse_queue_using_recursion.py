def enqueue(queue, item):
	queue.append(item)

def isEmpty(queue):
	return len(queue)==0

def dequeue(queue):
	if(isEmpty(queue)):
		return
	return queue.pop(0)



def reverse(queue):
	if isEmpty(queue):
		return ""
	x=dequeue(queue)
	reverse(queue)
	enqueue(queue, x)

	return queue





string = input()
queue = list(string)


result = reverse(queue)
print("".join(result))
