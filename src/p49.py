import math

limit=10000
P=[] #contains all prime nums smaller than limit
def isPrime(n):
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
		if isPrime(i):
			P.append(i)
	print 'generate P finished'		
fillP()	
print 'P is filled'		


def isPermutation(a,b):
	'''return true if digits of a are permutations of b'''
	sa,sb= str(a), str(b)
	for i in range(0,len(sa)):
		if sa.count (sa[i]) != sb.count(sa[i]): return False
	for i in range(0,len(sb)):
		if sa.count (sb[i]) != sb.count(sb[i]): return False	
	return True

# print isPermutation(1234,4231)		
# print isPermutation(1234,42315)		

def main():
	for a in P:
		for b in P:
			if a < b and isPermutation(a,b)  and isPermutation(2*b -a,a) and 2*b -a  in P:
				print a,b,2*b-a
main()	