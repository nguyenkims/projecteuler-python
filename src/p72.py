import math
import functions


P=[]
def fillP()	:
	for i in range(2, 10**3):
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
	return n

print smallestPrime(6), smallestPrime(29)	

limit = 10 ** 6 +1
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
# print PHI[9], PHI[87109]


def main():
	s = 0
	for n in range(2,limit):
		s += PHI[n]
	print 'sum',s
main()		