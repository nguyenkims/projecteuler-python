N=10 ** 10

def lastTenDigits(n):
	'''find last ten digits of n**n'''
	s=1
	for i in range(0,n):
		s = (s*n) % N
	return s

def main(n):
	'''calculate sum of lastTenDigits(k) with k from 1 to n'''
	s=0
	for k in range(1,n+1):
		s+= lastTenDigits(k)
	return s % N	
print main(1000)		