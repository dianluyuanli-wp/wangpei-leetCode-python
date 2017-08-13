class Interval(object):
	def __init__(self, s=0, e=0):
		self.start = s
		self.end = e
		
p1=Interval(1,4)
p2=Interval(2,3)
p3=Interval(3,4)

class Solution(object):
			
	def findRightInterval(self, intervals):
		int_copy = sorted((e.start, i) for i, e in enumerate(intervals))
		ans=[]
		ans_true=[]
		for inter_ele in intervals:
			index_l=0
			index_h=len(int_copy)
			index_mid=index_h//2
			if inter_ele.end>int_copy[-1][0]:
				ans.append([inter_ele.start,-1])
				continue
			while index_h-index_l is not 1:
				index_mid=index_l+(index_h-index_l)//2
				if int_copy[index_mid][0]<inter_ele.end:
					index_l=index_mid
				else:
					index_h=index_mid
			ans.append([inter_ele.start,index_h])
		ans_kk=[]
		for i in ans:
			ans_kk.append(i[0])
		for ii in intervals:
			ans_num=ans[ans_kk.index(ii.start)][1]
			if ans_num is not -1:
				ans_true.append(int_copy[ans_num][1])
			else:
				ans_true.append(-1)
		return ans_true

ps=[p1,p2,p3]

#~ print ps[1].start		
print Solution().findRightInterval(ps)


