# -*- coding: utf-8 -*-
import math
limit = 100000
P=[] #list of all primes smaller than limit

def isPrime(n):
	if n<2 : return False
	if n==2 : return True
	if n%2 ==0 :return False
	t = int(math.sqrt(n))
	#print n,t
	for i in range(2,t+1):
		if n % i == 0:
			#print i,n
			return False
	return True

def fillP():
	'''filling li'''
	for i in range(2,limit):
		if isPrime(i):
			P.append(i)

fillP()
print "filling P complete"

def isSquare(n):
	t = int(math.sqrt(n));
	#print n,t
	if t*t == n:
		return True
	else:
		return False

#print isSquare(17)
#print isSquare(16)
#print isSquare(15)

def isSearched(n):
	if n%2 == 1 and n not in P :
		for j in range(2,n):
			if (n-j)%2 == 0 and isPrime(j) and isSquare((n-j)/2):
				#print n,j, (n-j)/2
				return False
		return True
	return False	


for n in range(2,limit):
	if isSearched(n):
		print n
		break