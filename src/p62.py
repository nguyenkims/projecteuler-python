# -*- coding: utf-8 -*-
import math

def isPermutation(a,b):
	'''test if a is a permutation of b'''
	sa,sb=str(a),str(b)
	if len(sa)!= len(sb) : return False
	for i in range(0,len(sa)):
		if sa.count(sa[i]) != sb.count(sa[i]) : return False

	return True

print isPermutation(123,113)
print isPermutation(11255,52151)

N=5
limit = 10 * 10 ** 3
C=[] #contains cubes of numbers from 0 to limit
# C = (a,a**3,marked) where marked is to determine if a has been scanned
for i in range(0,limit):
	C.append([i,i**3,False])
print 'C is filled'

def main():
	for (a,ca, stat) in C:
		if a>0 and not stat:
			C[a][2] = True
			firstLetter=float(str(ca)[0])
			# print ca,firstLetter
			k1=math.exp(math.log(10/firstLetter) /3.0) #firstLetter* k1**3 >=10
			k2=math.exp(math.log(firstLetter) /3.0) # k2**3 <=firstLetter
			t1,t2=int(a/k2), int(a*k1)
			pa= [(b,cb,sb) for (b,cb,sb) in C[t1:t2] if isPermutation(ca,cb)]
			# pa= [(b,cb,sb) for (b,cb,sb) in C if isPermutation(ca,cb)]
			for (b,cb,sb) in pa:
				C[b][2] = True
			if len(pa) >= N:
				print pa
				break
	
def bruteForce():
	for (a,ca, stat) in C:
		pa= [(b,cb,sb) for (b,cb,sb) in C if isPermutation(ca,cb)]
		if len(pa) >= N:
			print pa
			break

	
main()
# bruteForce()
def test():
	a = 12
	print math.exp(math.log(a)/3)
# test()	














