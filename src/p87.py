import functions
import math
import time

MAX = 50000000 # * 10 ** 6

limit2 = int(math.sqrt(MAX))
limit3 = int(math.exp(math.log(MAX)/3))
limit4 = int(math.exp(math.log(MAX)/4))
print limit2,limit3,limit4
P=[]
def fillP():
	for i in range(2,limit2):
		if functions.isPrime(i):
			P.append(i)
	print 'P is filled', len(P)
fillP()			
P2=[p*p for p in P ]
P3=[p*p*p for p in P if p <= limit3]
P4=[p ** 4 for p in P if p <= limit4]
print 'P2,P3,P4 are filled', len(P2) * len(P3) * len(P4)



def main():
	'''lighter version
	Instead of all stocking in X, X is divided into part parts, so the test
	s in X is lighter'''
	part = 1000
	M = MAX/part
	X=[]
	for i in range(0,part): X.append([])
	start = time.time()
	for p2 in P2:
		for p3 in P3:
			for p4 in P4:
				s = p2 + p3 + p4
				if s < MAX :
					k = s / M
					# print s,p2,p3,p4,k

					if s not in X[k]:
						X[k].append(s)

					# X.append(s)
				# if len(X) % 1000 == 0:
				# 	print 'len',len(X)	
	final = 0			
	for i in range(0,part):	
		# print X[i]		
		final+= len(X[i])
	print 'main:final', final,'time', time.time() - start
main()		

def main2():
	'''heavier version because use only Y to stock all the results
	Note that the test s in Y is the most time-consuming one'''
	Y= []
	start = time.time()
	for p2 in P2:
		for p3 in P3:
			for p4 in P4:
				s = p2 + p3 + p4
				if s < MAX and s not in Y:
					Y.append(s)
	print 'main2:final', len(Y), 'time', time.time() - start
# main2()					