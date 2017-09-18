white=10
year=4
sum_n=0
qian=0
qu=0
for i in range(1,year+1):
	if i==1:
		sum_n+=white+white*2
		qu=white*2
		die=white
		#print sum_n
	elif i==2:
		sum_n+=white*3+qu*2
		qian=qu
		qu=white*3+qu*2
		#print sum_n
	else:
		sum_n+=qu*2+qian*3-die
		die=qian
		tt=qu
		qu=qu*2+qian*3
		qian=tt

sum_bb=0
qu=0
qian=0	
for i in range(1,year+1):
	if i==1:
		sum_bb+=white+white*3
		#//print sum_bb
	elif i==2:
		sum_bb+=white*3*3-white
		qu=white*3*3
		die=white*3
		#print sum_bb
	else :
		sum_bb+=qu*3-die
		die=qu
		qu=qu*3

print sum_n
print sum_bb		
print abs(sum_n-sum_bb)%10007
		
		
