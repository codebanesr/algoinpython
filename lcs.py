from functools import lru_cache

@lru_cache(maxsize=None)
def lcs(s, t):

	if len(s)==0 or len(t)==0:
		return 0
	if s[-1]==t[-1]:
		return 1+lcs(s[:-1], t[:-1])
	else:
		return max(lcs(s[:-1], t), lcs(s, t[:-1]))



print(lcs("AGGTAB", "GXTXAYB"))
