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

def is_prime2(n):
	'''using P to decide if n is prime faster'''
	i=0
	while i < len(P) and P[i] < n:
		i+=1
	if i < len(P) and P[i] == n:
		return True
	return False	 

def circular_combination(n):
	'''return circular combination with digits of n
	ex: 123-> 123,231,312'''
	s=str(n)
	li=[]
	if len(s) == 1:
		li.append(n)
		return li
	else:
		for i in range(0,len(s)):
			t=int(s[i:]+s[0:i] )
			if t not in li:
					li.	append(t)
		return li			


def is_circular_prime(n):
	'''test if n is a circular prime
	apply only for n > 10'''
	if n < 10 and is_prime(n)	:
		return True
	s = str(n)
	if  s.find('0')>=0 or s.find('2')>=0 or s.find('4')>=0 or s.find('8')>=0 or s.find('5')>=0:
		return False
	for i in circular_combination(n)	:
		if not is_prime2(i) :
		# if not i in P:
			# print 'i=',i
			return False
		
	return True

def test():
	print circular_combination(197)	
	print circular_combination(19)	
	if 197 in P and 971 in P and 719 in P:
		print 'ok'
	# if is_circular_prime(197):
	# 		print 'ok'
	if is_circular_prime(19):
		print 'strange'
 	print is_prime(91)	, 91 in P
# test()

def main()		:
	s=0
	for i in P:
		if is_circular_prime(i):
			s+=1
			print i
	print 'answer:',s		
main()			