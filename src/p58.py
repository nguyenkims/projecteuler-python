import math

limit=15000
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
print P[len(P) -1]

SP=[] #SP[n] contains nbSpriralPrimes(n):number of prime corresponding
	  # to a spiral with side length 2*n+1
def fillSP():
 	SP.append(0)
	SP.append(3)
	for n in range(2,limit):			
		bottomRight= (2*n+1) ** 2
		bottomLeft = bottomRight - 2*n
		topLeft= (2*n-1) ** 2 + 4 *n
		topRight= (2*n-1) ** 2 + 2 *n	
		count = 0
		if isPrime(bottomLeft): count +=1
		if isPrime(topLeft): count +=1
		if isPrime(topRight): count +=1
		SP.append(SP[n-1] + count)
fillSP()
print 'SP is filled'
print SP[3]

def nbOnDiagonal(n):
	'''return #numbers on the diagonal of a spiral with side length 2 *n +1'''
	return 4*n +1

def main():
	rate = 10
	n=0
	while True  :
		n+=1
		# print n, SP[n], nbOnDiagonal(n),2 *n +1
		# if n > 5: break
		if  SP[n] <= nbOnDiagonal(n) /rate:
				print n, SP[n], nbOnDiagonal(n),2 *n +1
				break
	
main()	