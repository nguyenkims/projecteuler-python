def hasDisctintDigit(n):
	'''test if all digits of n are distinct'''
	s = str(n)
	for i in range(0,len(s)-1):
		for j in range(i+1,len(s)):
			if s[i] == s[j]:
				return False
	return True			

def isOK(n,k)	:
	''' test if n, n*2,...,n*k can form a pandigital'''
	if not hasDisctintDigit(n):		return -1
	s=""	
	for i in range(1,k+1):		s+= str(n*i)
	# print s	
	if not hasDisctintDigit(s): return -1
	for i in range(1,10):
		if s.find(str(i)) < 0: return -1
	
	return int(s)		
def pandigital(n)	:
	'''return the pandigital corresponding to n if exists k such that isOK(n,k)'''
	m = 9 / len(str(n))
	for k in range(2,m +1):
		if isOK(n,k) > 0: return isOK(n,k)
	
limit=10000	
print isOK(192,3)	
print pandigital(192)
def main():
	m=-1
	for i in range(1,limit):
		t = pandigital(i)
		if t >0: print i,t
		if t > m: m = t
	print 'max:',m	
main()		