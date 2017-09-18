m=1
n=2

x,y=m,n

print(x)
print(y)

def gcd(m,n):
	if n==0:
		m,n=n,m
	while m!=0:
		m,n=n%m,m
	return n
	
b=gcd(30,60)
print("b="+str(b))

def Prim(graph):
	vnum=graph.vertex_num()
	mst=[None]*vnum
	cands=PrioQueue([0,0,0])
	count=0
	while count<vnum and not cands.is_empty():
		w,u,v=cands.dequeue()
		if mst[v]:
			continue
		mst[v]=((u,v),w)
		count+=1
		for vi,w in graph.out_edges(v):
			if not mst[vi]:
				cands.enqueue((w,v,vi))
	return mst



	
