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
