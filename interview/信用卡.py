while True:
	try:
		b=raw_input()
		if not b:
			break
		a=map(int,b.split())
		#print a
		ans=0
		#print ans
		for i in range(1,a[2]+1):
			if i%a[0]==0 and i%a[1]==0:
				ans+=1
		print ans
	except:
		break
