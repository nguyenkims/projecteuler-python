def fac(n):
	'''return n!
	'''
	if n==0:
		return 1
	else:
		return fac(n-1)*n

def digitSum(n):
	'''return the sum of digits of n
	'''		
	if n < 10:
		return n
	else:
		return n%10 + digitSum(n/10)

N = fac(100)		
print N
print digitSum(N)