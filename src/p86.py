import math
def isSquare(n):
	t = int(math.sqrt(n))
	if n == t * t:
		return True
	return False

maximum = 2000
limit = 1* 10**6

def findShortest(a,b,c):
	t = [a,b,c]
	x = sorted(t)[0]
	y = sorted(t)[1]
	z  = sorted(t)[2]
	
	m = (x+y)*(x+y) + z*z
	n = int(math.sqrt(m))
	if m == n*n:
		# print 'minimum',	n
		# 		print x,y,z,m,n
		return n
	return -1	

# findShortest(6,5,3)	
			
	
def nbSolution(M):
	count = 0
	for a in range(1,M+1):		
		for b in range(a,M+1):
			for c in range(b,M+1):
				if findShortest(a,b,c) > 0:
					# print a,b,c, findShortest(a,b,c)
					count +=1
	# print 'count', count	
	return count
test = [10,20,21]
for t in test: 
	print nbSolution(t)

numberSolution = []
def fillNumberSolution():
	'''fill numberSolution'''
	for i in range(maximum):
		numberSolution.append(0)
	for i in range(10)	:
		numberSolution[i] = nbSolution(i)
	for i in range(10,maximum)	:
		count, t = 0, 0
		for s in range(2,2*i+1):
			if isSquare(s*s+i*i):				
				if s <=i+1:
					count += s/2
				else:
					count += (2*i -s +2) /2	
		
		numberSolution[i] = numberSolution[i-1] + (count+t)			
	print 'numberSolution is filled'	

	
fillNumberSolution()
for t in test:		
	print numberSolution[t]
	
def main()		:
	print numberSolution[maximum-1]
	for i in range(maximum):
		if numberSolution[i] > limit:
			print 'found',i, numberSolution[i]
			return
main()				