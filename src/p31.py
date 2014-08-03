'''regroup terms by:
(a1 + 5*a5) + 2 * (a2 + 5* a10) +  20 (a20 + 5*a100 ) + 50 (a50 + 4*a200) 
'''

def f(n,a,b):
	''' #{x,y} so a*x + b*y = n'''
	s=0
	for i in range(0,n/a+1):
		for j in range(0,n/b+1):
			if a*i + b*j == n:
				s+=1
	return s
	
# print f(5,1,2)		

def g(n):
	'''central function'''		
	s=0
	for x1 in range(0,n/1+1):
		for x2 in range(0,n/2+1):
			for x20 in range(0,n/20+1):
				for x50 in range(0,n/50+1):
					if x1 + 2*x2 + 20*x20 + 50*x50 == n:
						s+= f(x1,1,5) * f(x2,1,5) * f(x20,1,5) * f(x50,1,4)
	return s
print g(200)					