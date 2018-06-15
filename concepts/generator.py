Three different ways of writing generators in python

def fib(n):
    counter,a,b = 0,0,1
    while counter<n:
        yield a
        a, b = b, a+b
        counter+=1

    
    
f = fib(5)
for x in f:
    print(x, end=' ')




def fib(n):
    counter,a,b = 0, 0, 1
    while True:
        if(counter>n):
            return
        yield a
        a,b = b,a+b
        counter+=1
        
f = fib(10)
for x in f:
    print(x, end=' ')
            



#printing infinite fibonacci sequence using generators
def fib():
    a,b = 0, 1
    while True:
        yield a
        a, b = b,a+b
    
    
f = fib()
counter = 0
for x in f:
    print(x, end=' ')
    if counter>10:
        break
    counter+=1
    
    
    
    
    