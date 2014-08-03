limit = 10000
round= 40
def isPalindromic(m)	:
	'''m is int'''
	n = str(m)
	N=len(n)
	for i in range(0,N/2 + 1):
		if n[i] != n [N-1-i]:
			return False
	return True
	
def reverse(n)	:
	'''ex: 123 -> 321'''
	s=""
	t = str(n)
	for i in range(len(t)-1,-1,-1):
		s =  s + t[i] 
	return int(s)	
print reverse(4213)	

def isLychrel(n)	:
	'''testing if n is lychrel in under 50 rounds'''
	r = 1
	t=n
	t = t+reverse(t)
	while r<round :
		if isPalindromic(t):
			# print n,r
			return False
		t = t+reverse(t)
		r+=1 
	return True	

print isLychrel(10677)	
def main()	:
	count =0
	for i in range(1,limit):
		if isLychrel(i):
			print i
			count += 1
	print 'answer:', count
main()			