# -*- coding: utf-8 -*-
import math
def f(n):
	'''return min a such that a**n >= 10 ** (n-1) '''
	if n==1: return 1
	a=0
	t=10**(n-1)
	while a **n < t:
		a+=1
	return a	

print f(10)

def main():
	s=0
	for n in range(1,30):
		if f(n) < 10:
			print n,f(n)
			s+= (10 - f(n))
	print 'answer:',s		
main()