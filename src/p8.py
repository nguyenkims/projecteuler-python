'''problem 8 in euler project
Using the fact that:
a+b > LIMIT/2
a+b < 2*LIMIT/3
and supposing a >= b
'''

def fun(a,b):
	'''return 0 if (a,b) is the right one
	'''
	return (LIMIT-a-b)*(LIMIT-a-b) - a*a - b*b

LIMIT = 1000
print 'LIMIT/2=', LIMIT/2
print 'LIMIT/3=', LIMIT/3

for a in range(LIMIT/4,LIMIT/2):
	for b in range( LIMIT/2 -a, a):
		if fun(a,b)==0 :
			print "we have found %d, %d" %(a,b)
			print 'product:', a*b*(LIMIT - a - b)
