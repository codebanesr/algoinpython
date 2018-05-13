#longest palindromic subsequence
from functools import lru_cache

@lru_cache(maxsize=None)
def lpalsub(s):
    if len(s)==1:
        return 1
    elif len(s)==2 and s[0]==s[1]:
        return 2
    
    
    if s[0] == s[-1]:
        return 2+lpalsub(s[1:-2])
    else:
        return max(lpalsub(s[1:]), lpalsub(s[:-1]))


print (lpalsub("DALDA"))