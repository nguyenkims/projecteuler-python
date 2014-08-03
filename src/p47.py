import math

limit=1000
P=[] #contains all prime nums smaller than limit
def is_prime(n):
	'''return True if n is prime
	False if not
	'''
	if n<2:
		return False
	root= int (math.floor(math.sqrt(n)))
	for i in range(2,root+1):
		if n % i == 0:
			return False;
	return True # n is prime

def fillP():
	'''Fills in P'''
	for i in range(0,limit):
		if is_prime(i):
			P.append(i)
	print 'generate P finished'		
fillP()	
print 'P is filled'		
# print P

def maxPower(n,p):
	'''return k max such that p ** k | n'''
	if n % p != 0 : return 0
	return 1 + maxPower(n/p,p)
	
print maxPower(36,2)	

def nbDistinctPrimeFactors(n):
	'''return the nb of prime factors of n'''
	if n==1: return 0
	root= int (math.floor(math.sqrt(n)))
	for p in [ x for x in P if x <= root]:
		if n % p == 0:
			k = maxPower(n,p)
			t = n / (p ** k)
			# print p,n,t
			return 1 + nbDistinctPrimeFactors(t)
	return 1
print nbDistinctPrimeFactors(150)			

def main()		:
	a = 10
	while 	nbDistinctPrimeFactors(a) <=3 or \
	 		nbDistinctPrimeFactors(a+1) <=3 or \
			nbDistinctPrimeFactors(a+2) <=3 or \
			nbDistinctPrimeFactors(a+3) <=3 :
			a += 1
	print a
# main()		

# m = 134043
# print nbDistinctPrimeFactors(m)	, nbDistinctPrimeFactors(m+1)	