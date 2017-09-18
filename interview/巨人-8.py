a=range(1,8+1)
print a
while len(a)>1:
	a.pop(0)
	b=a.pop(0)
	a.append(b)
	
print a
