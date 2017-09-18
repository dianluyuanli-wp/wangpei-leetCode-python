a=10
stack=[]
while True:
	try:
		a=raw_input()
		if not a:
			break
		a=int(a)
		stack=[]
		while a!=0:
			if a%2==0:
				stack.append('2')
				a=(a-2)/2
			else:
				stack.append('1')
				a=(a-1)/2
		stack.reverse()
		b=''.join(stack)
		print b
	except:
		break
	
		
