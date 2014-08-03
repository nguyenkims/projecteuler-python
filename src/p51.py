import functions

limit =  2* 10 ** 5
P=[] # set of primes smaller than limit
def fillP():
	'''filling P'''
	for i in range(2,limit):
		if functions.isPrime(i):
			P.append(i)
	print "filling P complete"	

fillP()

print 'length of P',len(P)


def generateSubsets(n):
	'''return the set of  all subsets of a {0,1,2,...,n-1}'''
	if n==1:
		return [[0]]
	else:
		k=[]
		t=generateSubsets(n-1)	
		# print t
		for x in t:	
			k.append(x)
			y=x+[(n-1)]
			k.append(y)
			# print x,y,k
		k.append([n-1])	
		return k
# print generateSubsets(4), len(generateSubsets(4)			)			

def s(p,S):
	'''return the number of primes when we replace all letters at positions
	corresponding to the set S '''
	sp=str(p)
	count = 0
	for s in S:
		if sp[s]!=sp[S[0]]:return -1
		
	if 0 in S: lower=1
	else: lower=0	
	
	for i in range(lower,10):
		sp1=""
		for j in range(0,len(sp)):
			if j in S: sp1 += str(i)
			else: sp1+=sp[j]
		if functions.isPrime(int(sp1))	:
			# print sp1
			count +=1
	return count

def f(p)	:
	'''return the maximum set of primes that we can generate from p'''
	Total=generateSubsets(len(str(p)))
	maximum=-1
	for S in Total:
		if s(p,S) > maximum:
			maximum = s(p,S)
			# print p,S
	return maximum		
	
	
def test()	:
	S=[0]			
	p=56003
	# print s(p,S)
	print f(p)
# test()	
# P = [x for x in P if x > 10**5 and x <limit]
def main():
	for p in P:
		if f(p) >=8:
			print p
			return
main()			