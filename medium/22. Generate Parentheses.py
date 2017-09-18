class Solution(object):
	ans=[]
	
	@classmethod
	def perm(cls,n,begin,end):
		tmp=''
		if begin>=end:
			for i in range(len(n)):
				tmp+=n[i]
			#print tmp
			Solution.ans.append(tmp)
			#print Solution.ans
		else:
			i=begin
			for num in range(begin,end):
				n[num],n[i]=n[i],n[num]
				cls.perm(n,begin+1,end)
				n[num],n[i]=n[i],n[num]
	
	@classmethod			
	def generateParenthesis(cls, n):
		kuohao,ans_true=[],[]
		for i in range(n):
			kuohao+='('+')'
		Solution.perm(kuohao,0,len(kuohao))
		k_list=list(set(Solution.ans))
		#print k_list
		for i in range(len(k_list)):
			flag=0
			test_k=[]
			for j in range(n*2):
				if k_list[i][j] is '(':
					test_k.append(k_list[i][j])
				elif k_list[i][j] is ')' and test_k:
					test_k.pop()
				else:
					break
				if j==n*2-1:
					flag=1
			if flag==1:
				ans_true.append(k_list[i])
		return ans_true
		
print(Solution().generateParenthesis(7))
