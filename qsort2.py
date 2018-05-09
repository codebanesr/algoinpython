def qsort(l):
    less, more, equal=[],[],[]
    if len(l)<2:
        return l#dont forget to return this array that only has one element otherwise you get nonetype error
    
    pivot = l[len(l)-1]
    for item in l:
        if item>pivot:
            more.append(item)
        elif item<pivot:
            less.append(item)
        else:
            equal.append(item)
        
        
    return qsort(less)+equal+qsort(more)
    
    
    
result = qsort([5,4,3,6,7,8])
print(result)
    
    
