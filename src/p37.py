import math

limit=1000000
P=[] #contains all prime nums smaller than limit
def is_prime(n):
	'''return True if n is prime
	False if not
	'''
	if n<2:
		return False
	root= int (math.floor(math.sqrt(n)))
	for i in range(2,root+1):
		if n % i == 0:
			return False;
	return True # n is prime

def fillP():
	'''Fills in P'''
	for i in range(0,limit):
		if is_prime(i):
			P.append(i)
	print 'generate P finished'		
fillP()			
# print P
# 
# 
def getTrunList(n):
	'''if n =abcd, returns abcd,abc,ab,a and bcd,cd,d'''
	li=[]
	s=str(n)
	for i in range(0,len(s)):
		t = s.__getslice__(0,len(s) - i)
		li.append(int(t))
	for i in range(1,len(s)):	
		k = s.__getslice__(i,len(s))
		li.append(int(k))
	return li
print getTrunList(1234)		

def isTruncatable(n):
	'''test if n is truncatable'''
	s = str(n)
	if n <10:
		return False
	for i in range(2,len(s)-3):
		if int(s[i])!=3 and int(s[i])!=9:
			return False
	if not is_prime(int(s[0])) or not is_prime(int(s[len(s)-1]))	:
		return False
	
	li = getTrunList(n)	
	for i in li:
		if i not in P:
			return False
	return True		
		
def main()			:
	nb,s=0,0
	for i in P:
		if isTruncatable(i):
			nb +=1
			s+= i
			print 'truncate:',i
	print 'nb of truncate number:',nb	
	print 'sum of truncate number:',s	
			
main()			