def isBalanced(expression):
	opening = tuple('({[')
	closing = tuple(')}]')

	mapping = dict(zip(opening, closing))
	print(mapping)

	stack = []
	for c in expression:
		if c in opening:
			stack.append(mapping[c])

		elif c in closing:
			if not stack or stack.pop()!=c:
				return False
	return not stack






if isBalanced("(()){{}}"):
	print("isBalanced")