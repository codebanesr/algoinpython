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
    
    
    
    
    


 #printing infinite integers using generators
 def integers():
    i = 0
    while True:
        yield i
        i+=1
        
        
i = integers()
counter = 0
for x in i:
    print(x, end=' ')
    counter+=1
    if counter>10:
        break



#printing infinite sequence of squares using generators
def squares():
    i = 0
    while True:
        yield i**2
        i+=1
s = squares()
counter = 0

for x in s:
    print (x, end=' ')
    counter+=1
    if counter>10:
        break
        