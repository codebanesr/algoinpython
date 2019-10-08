# 1. It should be stack sortable
# which also means it should not have 2-3-1 pattern (low-high-very.low)


def isbstpreorder(iterable):
    lowerbound = None
    stack = []
    for x in iterable:
        if lowerbound is not None and x < lowerbound: return False
        while stack and stack[-1] < x: lowerbound = stack.pop()
        stack.append(x)
    return True
    
    
    
https://stackoverflow.com/questions/26173808/checking-if-given-preorder-traversal-is-valid-bst
    
    
    
    
#     How to check for 231 pattern
mark first node as root, wait for the next greater node and mark it as root,

if a node greater than this arrives we have reached our first partition

lets mark it as the root, now after this we can have element greater or smaller than the root
if we get an element greater than this we keep that element in the stack, remember we havent changed the root but what we have
is the root of the RST and remember for RST we can never have an element greater than the root. If it happens just return false;
everytime you get an element greater than the element on stack we are moving furthur right and can never have an element less
than the root....... That ends the discussion not completely
