class Interval(object):
	def __init__(self, s=0, e=0):
		self.start = s
		self.end = e
		
p1=Interval(1,4)
p2=Interval(2,3)
p3=Interval(3,4)

class Solution(object):
	def merge(self,lfrom,lto,low,mid,high):					
		i,j,k=low,mid,low							
		while i<mid and j<high:						
			if lfrom[i].start<=lfrom[j].start:
				lto[k]=lfrom[i]
				i+=1
			else:
				lto[k]=lfrom[j]					
				j+=1							
			k+=1
		while i < mid:
			lto[k]=lfrom[i]
			i+=1
			k+=1
		while j<high:
			lto[k]=lfrom[j]
			j+=1
			k+=1

	def merge_pass(self,lfrom,lto,llen,slen):				
		i=0											
		while i+2*slen<llen:							
			self.merge(lfrom,lto,i,i+slen,i+2*slen)
			i+=2*slen
		if i+slen<llen:								
			self.merge(lfrom,lto,i,i+slen,llen)
		else:
			for j in range(i,llen):							
				lto[j]=lfrom[j]

	def merge_sort(self,lst):
		slen,llen=1,len(lst)
		bb=Interval(0,0)
		templst=[]
		for i in range(len(lst)):
			templst.append(bb)
		while slen<llen:								
			self.merge_pass(lst,templst,llen,slen)	
			slen*=2
			self.merge_pass(templst,lst,llen,slen)
			slen*=2
			
	def findRightInterval(self, intervals):
		int_copy=list(intervals)
		self.merge_sort(int_copy)
		ans=[]
		ans_true=[]
		for inter_ele in int_copy:
			index_l=0
			index_h=len(int_copy)
			index_mid=index_h//2
			if inter_ele.end>int_copy[-1].start:
				ans.append([inter_ele.start,-1])
				continue
			while index_h-index_l is not 1:
				index_mid=index_l+(index_h-index_l)//2
				if int_copy[index_mid].start<inter_ele.end:
					index_l=index_mid
				else:
					index_h=index_mid
			ans.append([inter_ele.start,index_h])
		for ii in intervals:
			ans_num=ans[int_copy.index(ii)][1]
			if ans_num is not -1:
				ans_true.append(intervals.index(int_copy[ans_num]))
			else:
				ans_true.append(-1)
		return ans_true

ps=[p1,p2,p3]

#~ print ps[1].start		
print Solution().findRightInterval(ps)


