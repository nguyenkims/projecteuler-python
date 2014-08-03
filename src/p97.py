#based on p48

N=10 ** 10
limit=7830457
A=28433
def lastTenDigits(n):
	'''find last ten digits of 2**n'''
	s=1
	for i in range(0,n):
		s = (s*2) % N
	return s

print (A*lastTenDigits(limit) +1 ) % N