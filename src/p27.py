LIMIT=1000
import math
pTab1,pTab2,pTab3=[],[],[] #correspond to primes N smaller than 1000 , 2000, LIMIT*LIMIT

def is_prime(n):
	'''return True if n is prime
	False if not
	'''
	root= int (math.floor(math.sqrt(n)))
	for i in range(2,root+1):
		if n % i == 0:
			return False;
	return True # n is prime

def is_prime2(n):
	'''ameliorated version of is_prime with assumption that pTab1 is generated
	'''
	root= int (math.floor(math.sqrt(n)))
	for i in pTab1:
		if n  % i == 0:
			return False;
	return True # n is prime

def fills_pTab():
	'''fills pTab1 ,pTab2, pTab3
	'''
	pTab1.append(2) 
	pTab1.append(3)
	for i in range(5,LIMIT):
		if is_prime(i):
			pTab1.append(i)

	pTab2.extend (pTab1	)
	for i in range(LIMIT, 2*LIMIT):
		if is_prime(i):
			pTab2.append(i)

	pTab3.extend(pTab2)
	for i in range(2*LIMIT, LIMIT*LIMIT):
		if is_prime2(i): #much better than using is_prime
			pTab3.append(i)		
			
def test():
	fills_pTab()
	print pTab3
	# print pTab2
	# print f(-996,997)
	# print f(1,41)
	# print f(-79,1601)
	print len(pTab1)
	print intersection(range(1,100), pTab1)
	if is_prime2(99991):
		print 'ok'
# test()	

def in2(n):
	'''testing if n is in pPab3
	Cannot use simply (if n in pTab3) because it takes a complete search -> 
	complexity=O(len(pTab3))'''
	t = 0
	while(True):
		if pTab3[t] == n:
			return True
		elif pTab3[t] < n:
			t += 1
		else:
			return False		

def f(a,b):
	'''returns the # prime numbers of n*n + a*n +b starting at n=0'''
	count,n = 0,0
	while (True):
		t = n *n + a * n + b
		if in2(t):
			count +=1
			n+= 1
		else:
			return count	

def main()	:
	M, A, B = -1,-1,-1
	fills_pTab()
	print 'generating finished'
	
	for x in pTab1:
		for y in pTab2:
			b,a = x, y - x -1
			if f(a,b) > M:
				M,A,B = f(a,b),a,b
	print M,A,B			
	
if __name__=="__main__":
	main()				
				
	