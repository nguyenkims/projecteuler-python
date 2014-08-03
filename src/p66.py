from functions import continuedFraction
import math
def fraction(pList):
	'''from the list pList = [a0 a1 a2 ...]
	returns the corresponding fraction P/Q '''
	length = len(pList)
	p,q = 1,0
	lP, lQ = [pList[0]], [1] 
	p1 = pList[1] * lP[0] + p
	q1 = pList[1] * lQ[0] + q
	lP.append(p1)
	lQ.append(q1)
	
	for i in range(2,length):
		# print lP,lQ
		pi = pList[i]* lP[i-1] + lP[i-2]
		qi = pList[i]* lQ[i-1] + lQ[i-2]
		lP.append(pi)
		lQ.append(qi)
	return [lP,lQ]	


def pellSolution(pNumber):
	'''return the solution of Pell equation x*x - pNumber*y*y = 1'''
	l = continuedFraction(pNumber, pNumber*2)
	# print l
	t = fraction(l)
	P,Q = t[0], t[1]
	for i in range(len(P)):
		pi,qi = P[i], Q[i]
		# print pi,qi
		if pi*pi- pNumber*qi*qi == 1:			
			return [pi,qi]

def test()	:
	l = [1,2,3,4]
	# print fraction(l)
	
	A = [2,3,5,6,7,61]
	for a in A:
		print pellSolution(a)
test()	

def main()	:
	maximum = -1
	limit = 1000
	for a in range(2,limit+1):
		t = int(math.sqrt(a))
		if a!= t*t:
			p= pellSolution(a)
			x = p[0]
			if x > maximum:
				maximum = x
				print a,p
main()				