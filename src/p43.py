# -*- coding: utf-8 -*-
P=[2,3,5,7,11,13,17]
def isPandigital(n):
	'''test if n is pandigital'''
	s = str(n)
	for i in range(0,len(s)):
		if s.find(str(i)) == -1 :
			return False
	return True

def g(i,n):
	'''s=str(n)
	if i =2 return s2s3s4
	i=3 returns s3s4s5'''
	t=""
	s=str(n)
	if i < 8:
		t+= str(s[i-1]) + str(s[i]) + str(s[i+1])
	#elif i==8:
		#t+= str(s[i-1]) + str(s[i]) + str(s[i+1])
	return int(t)
	
print g(2,1406357289)	,g(3,1406357289)

def isInteresting(n):
	'''test if n satisfies the characteristics in problem 43'''
	for i in range(2,8):
		if g(i,n) % P[i-2] != 0:
			#print i,n
			return False
	return True

#print isInteresting(1406357289)

def f(a,b):
	'''if a =1, b=234 returns 123'''
	s=str(a)
	s = s+ str(b)[0] + str(b)[1]
	return int(s)
	
print f(7,289)	
def main():
	for i in range(1,1000):
		if i % 17 == 0 and isPandigital(i): #find d8d9d10
			for d
			