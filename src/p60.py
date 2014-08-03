import math


limit=10000
P=[] #contains all prime nums smaller than limit

def isPrime(n):
	'''return True if n is prime
	False if not
	'''
	if n<2:
		return False
	if n < limit * limit :
		root= int (math.floor(math.sqrt(n)))
		for i in range(2,root+1):
			if n % i == 0:
				return False;
		return True # n is prime
	else:
		for i in P:
			if n % i ==0: return False
		root= int (math.floor(math.sqrt(n)))
		for i in range(P[len(P)-1], root )	:
			if i % 2 !=0 and i %3 != 0 and n % i ==0: return False
		return True	
					

def fillP():
	'''Fills in P'''
	for i in range(0,limit):
		if isPrime(i):
			P.append(i)

fillP()	
print 'P is filled'

def isConcatenable(p,q):
	'''test if pq and qp are primes'''
	if 5 in [p,q] or 2 in [p,q]: return False
	if q > 3 and p > 3 and (p-q) % 3 != 0:return False
	sp,sq= str(p), str(q)	
	if isPrime(int(sp+sq)) and isPrime(int(sq+sp)): return True

def isOK(p,s):
	'''s = list of some primes, p is prime
	test if concatenation of p with each member of s are primes
	 (and inversely) '''	
	for q in s:
		if not isConcatenable(p,q): return False
	return True	

fourPrimes=[] #contains all 4 primes satisfying concatening property
def main()	:
	for a in P:	
		pa= [p for p in P if p >a and isConcatenable(p,a) ]
		for b in pa:
			pb = [p for p in pa if p > b and isConcatenable(p,b)]
			for c in pb:
				pc = [p for p in pb if p >c and  isConcatenable(p,c)]			
				for d in pc:
					pd=	[p for p in pc if p >d and  isConcatenable(p,d)]					
					if len(pd) > 0:
						print a,b,c,d,pd[0], a+b+c+d+pd[0]
						return

main()			



