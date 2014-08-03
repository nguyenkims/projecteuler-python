from functions import isPrime
P = []
for a in range(2,400):
	if isPrime(a): P.append(a)
print P	

def smallestPrime(pN):
	'''return the smallest prime divisor of pN'''
	for p in P:
		if pN % p == 0:
			return p
	return pN
			
limit = 10**5
L = [0,1] #L[n] = rad(n) 			
def fillL():
	n = 1
	while n < limit:
		n+=1
		p = smallestPrime(n) 
		t = n/p
		# print n,p,t
		if t % p == 0:
			L.append(L[t])
		else:	
			L.append(L[t]*p)
	print 'L is filled'
fillL()			
def test():
	for i in range(limit)	:
		# print i,L[i]
		pass
	k = sorted(L)	
	print k[3], k[5]
	
test()	

def main():
	print L
	pos = 10000
	K = sorted(L)
	x = K[pos -1]
	p = pos -1
	while K[p] == x:
		p -=1 
		
	gap = pos - 1 -p	
	count = 0
	for i in range(limit):
		if L[i] == x :
			count +=1
			if count == gap+1:
				print 'found',i,x
main()			