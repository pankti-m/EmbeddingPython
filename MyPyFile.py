def operation(op, x, y):
	return {
		'+': x+y,
		'-': x-y,
		'*': x*y,
		'/': x/y
	}.get(op, "Error")


print "**Python execution starts**"
while True:
	#get operation
	op = raw_input('Enter the operation(+,-,*,/): ')

	#get first arg
	x = int(raw_input('Enter the 1st argument: '))

	#get second arg
	y = int(raw_input('Enter the 2nd argument: '))

	result = operation(op, x, y)
	print x,op,y,'=',result
