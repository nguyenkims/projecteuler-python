import math
import functions

def isPermutation(a,b):
	'''return true if digits of a are permutations of b'''
	sa,sb= str(a), str(b)
	for i in range(0,len(sa)):
		if sa.count (sa[i]) != sb.count(sa[i]): return False
	for i in range(0,len(sb)):
		if sa.count (sb[i]) != sb.count(sb[i]): return False	
	return True
P=[]
def fillP()	:
	for i in range(2, 3* 10**3):
		if functions.isPrime(i): P.append(i)
	print 'P is filled'
fillP()
print P[0], P[1], len(P)		
def smallestPrime(n):
	if n<2 : return 1
	if n%2 ==0 :return 2
	t = int(math.sqrt(n))
	for p in P:
		if p <= t and n % p == 0:
			return p
	#print n,t
	# for i in range(2,t+1):
	# 		if n % i == 0:
	# 			#print i,n
	# 			return i
	return n

print smallestPrime(6), smallestPrime(29)	


limit = 10 ** 6
PHI=[]
def fillPHI():
	PHI.append(0)
	PHI.append(1)
	for n in range(2,limit):
		p = smallestPrime(n)
		if p == n:
			PHI.append( p-1)
		else:
			m = n/p
			if m % p == 0:
			 	PHI.append(PHI[m] * p)
			else:
				PHI.append(PHI[m] * (p-1))
	print 'PHI is filled'		
fillPHI()	
print PHI[9], PHI[87109]
def phi(n):
	if n < limit: return PHI[n]
	p = smallestPrime(n)
	if p == n:
		return p-1
	m = n/p
	if m % p == 0:
		return phi(m) * p
	return phi(m) * (p-1)	
print phi(9), phi(87109), phi(8584933)

def main():
	minimum = limit
	n = 2
	while n < 10 * limit:
		# t = PHI[n]
		if n < 1000  or (smallestPrime(n) > 1000): #ignore the  numbers with a small divisor
			t = phi(n)
			if isPermutation(n,t):
				if float(n)/float(t) < minimum:
					minimum = float(n)/float(t)
					print 'found',n,t,minimum
		n+=1		
main()	