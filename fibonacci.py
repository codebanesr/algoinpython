from functools import lru_cache


@lru_cache(maxsize=None)
def fibonacci(n):
	if n==1 or n==0:
		return 1

	else:
		return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(9))