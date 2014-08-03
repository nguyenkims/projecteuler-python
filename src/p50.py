import math

limit=20000
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


def test():
	s,count=0,0
	for a in P :
		if count < 21:	
			s+=a
			print a,s
			count +=1
		else: break	
	print s	

LIMIT= 10 ** 6
def findPrimeWithTerm(k):
	'''find all prime numbers that is the sum of k consecutive prime numbers
	'''
	s=0
	for i in range(0,len(P) - k):
		if i ==0:
			for j in range(0,k): s+= P[j]
		else:
			s = s - P[i-1] + P[i+k-1]	
		if is_prime(s): 			
			if s < LIMIT:
				print P[i],k,s	
				return True
			else:
				return True
		# print P[i],k,s
print is_prime(978037)
def main():
	k = 21
	while findPrimeWithTerm(k)	:
		k=k+2			
main()	
# findPrimeWithTerm(540)
# findPrimeWithTerm(541)
# findPrimeWithTerm(543)