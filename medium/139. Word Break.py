class Solution(object):
	def wordBreak(self, s, wordDict):
		num,stack,stack_1=[],[],[]
		if not wordDict:
			return False
		for x in wordDict:
			if len(x) not in num:
				num.append(len(x))
		i=len(s)
		while i!=0 or stack:
			for x in num:
				if i>=x:
					if s[i-x:i] in wordDict:
						if i-x==0:
							return True
						if i-x not in stack_1:
							stack_1.append(i-x)
							stack.append(i-x)
			if not stack:
				return False
			i=stack.pop()
		return False
s='leetcode'
dict_u=["leet", "code"]
cc="bccdbacdbdacddabbaaaadababadad"
cc_t=["cbc","bcda","adb","ddca","bad","bbb","dad","dac","ba","aa","bd","abab","bb","dbda","cb","caccc","d","dd","aadb","cc","b","bcc","bcd","cd","cbca","bbd","ddd","dabb","ab","acd","a","bbcc","cdcbd","cada","dbca","ac","abacd","cba","cdb","dbac","aada","cdcda","cdc","dbc","dbcb","bdb","ddbdd","cadaa","ddbc","babb"]
aa="acaaaaabbbdbcccdcdaadcdccacbcccabbbbcdaaaaaadb"
dict_=["abbcbda","cbdaaa","b","dadaaad","dccbbbc","dccadd","ccbdbc","bbca","bacbcdd","a","bacb","cbc","adc","c","cbdbcad","cdbab","db","abbcdbd","bcb","bbdab","aa","bcadb","bacbcb","ca","dbdabdb","ccd","acbb","bdc","acbccd","d","cccdcda","dcbd","cbccacd","ac","cca","aaddc","dccac","ccdc","bbbbcda","ba","adbcadb","dca","abd","bdbb","ddadbad","badb","ab","aaaaa","acba","abbb"]	
bb="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
bb_t=["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
print Solution().wordBreak(bb,bb_t)

					
