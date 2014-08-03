# -*- coding: utf-8 -*-
import math
li=[]
biggerLi=[]
limit=5000
out=file("p44_output.txt", "w")

for i in range(1,limit):
	li.append(i * (3*i-1)/2)
for i in range(1,2*limit):
	biggerLi.append(i * (3*i-1)/2)

def f(t):
	return t*(3*t-1)/2
	
def isPentagonal(n):
	t = int(math.floor(math.sqrt(2*n/3))) +1
	#print 't=',t
	if f(t) == n :
		return True
	return False
print isPentagonal(22)

print 'finished generating li and biggerLi'

sumCouple=[]
for i in li:
	#for j in [x for x in li if x <i]:
	for j in li:
		#if (i-j) in li and (i+j) in biggerLi:
		#if  (i+j) in biggerLi:
		if isPentagonal(i+j):
				#print i,j,i+j
				if i>j:
					sumCouple.append((i,j))
					out.write(str((i,j)))
				else:
					sumCouple.append((j,i))
					out.write(str((j,i)))
				#print li.index(i), li.index(j),li.index(i+j)

print 'finished generating sumCouple'

for (i,j) in sumCouple:
	if isPentagonal(i-j):
		print i,j,i-j

				