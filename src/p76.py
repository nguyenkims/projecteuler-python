# -*- coding: utf-8 -*-
limit=100
def nb(n,a):
	'''nb of different ways to write n as the sum of numbers
	that are all greater or egal to a'''
	if a == n or n==0 : return 1
	if a >n: return -1
	s=0
	for b in range(a,n+1):
		if nb(n-b,b) > 0:
			#print n,b, nb(n-b,b)
			s+= nb(n-b,b)
	return s

# can not calculate directly from nb(n,a) because it takes too much of time, due to
# the fact that the value isn't stocked during the process

A=[] #A[n][a] = nb(n,a)
for n in range(0,limit+1):
	A.append([])
	for a in range(0,limit+1):
		A[n].append(0)

for n in range(0,limit+1):
	for a in range(1,limit+1):
		if a == n or n==0 :  A[n][a] = 1
		elif a >n: A[n][a] = -1
		else:
			s=0
			for b in range(a,n+1):
				if A[n-b][b] > 0:
					#print n,b, nb(n-b,b)
					s+= A[n-b][b]
			A[n][a] = s
		
print  nb(5,1) - 1
print A[limit][1] -1