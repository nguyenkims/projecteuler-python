# -*- coding: utf-8 -*-
import math

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

print isPrime(1001)
print isPrime(69)
print isPrime(3)

def isPandigital(n):
	'''test if n is pandigital'''
	s = str(n)
	for i in range(1,len(s)+1):
		if s.find(str(i)) == -1 :
			return False
	return True

m=-1
for i in range(1,10):

	if i % 3 == 1: #because if not, 3 will divide the corresponding pandigital  
		limit=10 ** (i-1)
		for n in range(limit,10*limit):
			if isPandigital(n) and isPrime(n):
				m=n
				#print n
print 'answer:',m