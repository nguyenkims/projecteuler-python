
def f(m,n):
	'''return the number of rectangles that a m x n contains'''
	s=0
	for a in range(1,m+1):
		for b in range(1,n+1):
			s+= (m-a+1)*(n-b+1)
	return s
print f(1,1),f(2,4), f(3,3)		

def g(m,n):
	''' the same as f(m,n) except g(m,n) is calculated recursively'''
	if m==0:
		return 0
	elif m == 1 :
		return n * (n+1) /2		
	else:
		return 2* g(m-1,n) - g(m-2,n) + n*(n+1)/2 
print g(1,1), g(2,1), g(2,3), g(3,3)

limit = 2 * 10 **6		
M=200
N=2000
L={} # L contains (m,n,f(m,n))
def fillL():
	for m in range(0,M):
		for n in range(0,N):
			if m==0:
				L[(m,n)]=0
			elif m == 1 :
				L[(m,n)] =  (n * (n+1)) /2		
			else:
				L[(m,n)] = 2* L[(m-1,n)] - L[(m-2,n)] + n*(n+1)/2
fillL()
print 'L is filled'				
# print L[(3,3)], L[(2,3)], L[(100,100)], L[(20,200)] , L[(672,854)]
def main()	:
	mimumum = 10 ** 6
	for m in range(1,M):
		for n in range(1, N):
			if m*n + n*(n+1) + m*(m+1)> 3*limit:
				pass
			else:
				t = L[(m,n)]
				# t= g(m,n)
				if abs(t - limit) < mimumum:
					mimumum = abs(t - limit)
					print m,n,t, m*n
main()				