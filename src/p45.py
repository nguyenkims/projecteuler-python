import math
def P(n):	return n*(3*n-1)/2
def H(n)	: return n*(2*n-1)

def isPentagonal(n):
	k = int(math.sqrt(2*n/3))
	if n == P(k+1):
		return True
	return False
	
print isPentagonal(35)	

i=minimum=143
while(True):
	i+=1
	if isPentagonal(H(i)):
		print H(i)
		break
		
	