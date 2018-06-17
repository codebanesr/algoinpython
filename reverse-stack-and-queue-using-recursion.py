def pop(stack):
    val = stack[-1]
    del stack[-1]
    return val

def push(stack, x):
    stack.append(x)

    
def pushBottom(stack, x):
    stack.insert(0, x)
    
def reverse(stack):
    if len(stack)==0:
        return 
    x=pop(stack)
    reverse(stack)
    pushBottom(stack, x)

stack = [1,2,3,4]
push(stack, 11)
reverse(stack)
print(stack)








#reverse queue using recursion
def enqueue(queue, x):
    queue.insert(0, x)
    
def dequeue(queue):
    x = queue[-1]
    del queue[-1]
    return x
    
def reverse(queue):
    if len(queue)==0:
        return
    x = dequeue(queue)
    reverse(queue)
    enqueue(queue, x)
    


q = [1,2,3,4,5]
reverse(q)
print(q)
