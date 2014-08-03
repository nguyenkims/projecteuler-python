# -*- coding: utf-8 -*-
import math

def isGreater(a,b,c,d):
	'''test if a**b > c**d'''
	#if a>c and b >d: return True
	#if a<c and b <d: return False

	fa,fb,fc,fd=float(a),float(b),float(c),float(d)
	#print fa,fb,fc,fd
	if fa> math.log(fc,fb) *fd:
		#print fa,math.log(fc,fb) *fd
		return True
	#if a**b > c**d :return True
	return False

print isGreater(632382,518061, 519432,525806  )
print isGreater( 519432,525806 ,632382,518061 )

inp=file("base_exp.txt")
A,B,T=[],[], []
t=inp.readline()
while t!= "":
	T.append(t)
	A.append(int(t.split(",")[0]))
	B.append(int(t.split(",")[1]))
	t=inp.readline()
#print A[0],B[0]
#print A[1],B[1]
#print T[0],T[1]
#print len(A)

def main():
	A.append(1)
	B.append(1)

	count=len(A) -1
	for i in range(0,len(A) -1):
	#for i in range(0,10):
		if isGreater(A[i], B[i], A[count], B[count]):
			count = i
			print i

	print 'answer:',count
	print A[count],B[count]
main()	