def deciToBina(n):
	'''convert n to binary mode, return string'''
	s=""
	while (n/2 > 0):
		s = str(n%2) +s
		n=n/2
	s = str(n)	+ s
	return s



def isPalindromic(n)	:
	'''n is string'''
	N=len(n)
	for i in range(0,N/2 + 1):
		if n[i] != n [N-1-i]:
			return False
	return True
def isOK(n):
	'''n is int, decide if n is palindromic in decimal and binary'''
	if n % 2==0: return False
	if not isPalindromic(str(n)):	return False
			
	b= deciToBina(n)	
	if not isPalindromic(b):		return False
	return True
		
def test()			:
	print deciToBina(8)		
	print isPalindromic("383")
	print isPalindromic("4114")
	print isOK(585)
	print deciToBina(717)
test()
limit=1000000

def main():
	s=0
	for i in range(0,limit):
		if isOK(i):
			print i
			s+=i
	print 'answer:',s		
	
main()	