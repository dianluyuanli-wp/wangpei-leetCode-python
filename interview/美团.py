while True:
	try:
		a=raw_input()
		if not a:
			break
		a=int(a)
		for i in range(a):
			b=raw_input()
			if len(b)<8:
				print "NO"
			elif not b.isalnum():
				print "NO"
			elif b[0].isdigit():
				print "NO"
			elif b.isdigit() or b.upper()==b or b.lower()==b:
				if b.isdigit():
					print "NO"
				elif b.upper()==b or b.lower()==b:
					flag=0
					for i in range(len(b)):
						if b[i].isdigit():
							print "YES"
							flag=1
							break
					if flag==0:
						print "NO"
			else:
				print "YES"
	except:
		break
		
		
