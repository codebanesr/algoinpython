#to be completed later


def toPostfix(infix):
	stack = []
	postfix = ''

	for c in postfix:
		if isOperator(c):
			postfix+=c
		else:
			if isLeftParanthesis(c):
				stack.append(c)

			elif isRightParanthesis(c):
				operator = stack.pop()
				while !isLeftParanthesis(operator):
					postfix+=operator
					operator = stack.pop()#left paranthesis automatically gets popped off

				else:
					while (not stack.isEmpty) and hasEqualOrLesserPriority(c, stack.peek()):
						postfix+=stack.pop()
					stack.append(c)

	while not isEmpty(stack):
		postfix+=stack.pop()

	return postfix