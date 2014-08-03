# -*- coding: utf-8 -*-
import math
limit= 10 ** 6
#limitN=int(math.sqrt(3*limit))
s=""
for i in range(1,limit):
	s+= str(i)

#print s
def d(i):
	'''return d[i]'''
	return int(s[i-1])

print d(12)
print d(11)
print d(10)


m=1
for i in range(0,7):
	print 10**i,d(10**i)
	m *= d(10**i)
print 'answer:',m	

