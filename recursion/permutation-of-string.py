#all permutations of a string

def findpermutation(s):
    result = set()
    if len(s) == 0:
        return result
    
    
    a = s[0] #take out the first character
    if len(s)==1:
        return set(a)
    
    intermediate = findpermutation(s[1:])# get the permutation for the remaining string first and then for each of those,
                                         #add a at every possible position
    
    
    
    for x in intermediate:               #for all the permutation of the substring
        for y in range(len(x)):          # add the first character at every possible location
            result.add(x[0:y]+a+x[y:])   # slicing it at every position from 0 till the length of the substring
            
    return result
    
s = "shanur"
res = findpermutation(s)

print(res)
    
    
