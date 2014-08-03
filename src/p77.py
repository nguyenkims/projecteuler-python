from functions import isPrime
numberPrimes = 100
P = []
def fillP():
	count, t = 0,2
	while count < numberPrimes:
		if isPrime(t):
			P.append(t)
			count +=1
		t+=1	
fillP()


def nb(n,a):
	'''nb of different ways to write n as the sum of numbers
	that are all greater or egal to P[a]'''
	if P[a] == n or n==0 : return 1
	if P[a] >n: return -1
	s=0
 	L = [i for i in range(len(P)) if i>=a]
	# print 'L',L
	for b in L:
		# print b,P[b], n - P[b], nb(n-P[b],b)
		if nb(n-P[b],b) > 0:
			s+= nb(n-P[b],b)
			# print n,b, P[b],  nb(n-P[b],b),s

	return s


limit=100
length = len(P)
print P, length
# can not calculate directly from nb(n,a) because it takes too much of time, due to
# the fact that the value isn't stocked during the process

def main():
	A=[] #A[n][a] = nb(n,a)
	for n in range(0,limit+1):
		A.append([])
		for a in range(0,length):
			A[n].append(0)

	for n in range(0,limit+1):
		for a in range(0,length):
			if P[a] == n or n==0 :  A[n][a] = 1
			elif P[a] >n: A[n][a] = -1
			else:
				s=0
				for b in range(a,length):
					if n >= P[b] and A[n-P[b]][b] > 0:
						# print n,b, nb(n-P[b],b)
						s+= A[n-P[b]][b]
				A[n][a] = s
		
	print  nb(5,0), A[5][0], A[limit][0] 
	n = 2
	while n < limit and A[n][0] <= 5000:
		n+=1
	print 'answer=', n, A[n][0]	
main()	