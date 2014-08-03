from functions import gcd, continuedFraction
import math

def properFraction(pNume,pDeno):
	'''pNume: numerator, pDeno: Denominator	
	return [z,x,y] such that pNume/pDeno =z +  x/y and gcd(x,y) = 1'''
	t = gcd(pDeno,pNume)
	z = pNume / pDeno
	x,y = (pNume - z*pDeno)/t, pDeno/t
	return [z,x,y]
print properFraction(20,15)	


print continuedFraction(13,10)

def fractionPeriod(pN): 
	'''return the period of continued Fraction of 
	squareRoot(n)'''
	squareRoot = int(math.floor(math.sqrt(pN)))
	length = 10 *squareRoot
	l = continuedFraction(pN, length)[1:]
	# print l
	k = 0
	nonSatisfy = True
	while nonSatisfy:	

		k+=1
		nonSatisfy = False
		for t in range(0,10):
			if (t+2)* k < length:
				if not nonSatisfy and l[t*k:(t+1)*k]!= l[(t+1)*k:(t+2)*k]:
					# print l[t*k:(t+1)*k], l[(t+1)*k:(t+2)*k]
					nonSatisfy = True
	return k

print fractionPeriod(7)
def test():
	A = [2,3,5,6,7,8,10,11,12,13]		
	for a in A:
		print a,fractionPeriod(a)				
# test()		

def main():
	limit = 10000
	count = 0
	for n in range(2,limit):
		t = int(math.sqrt(n))
		if t * t != n:
			period = fractionPeriod(n)
			if period % 2 == 1:
				print n,period
				count +=1
	print 'count', count
main()				
				

