# -*- coding: utf-8 -*-
import math
N=10 ** 6
limit = 10000
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

a,count=1,0
while a < N:
	a*=P[count]
	print P[count],a
	count+=1
print a	