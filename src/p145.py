def f(n):
	'''return the number of couple (a,b) such that a+b = n and a,b <10
	and a,b >=0'''
	if n < 10 and n>=0:
		return n+1
	elif n < 19 and n>=10:
		return 10 - (n-9) 	
	else: 
		return 0
print f(12)	, f(6)		
def g(n):
	'''return the number of couple (a,b) such that a+b = n and a,b <10
	and a >0, b>0'''
	if n < 10 and n>=2:
		return n-1
	elif n < 19 and n>=10:
		return 10 - (n-9) 	
	else: 
		return 0
print g(9), g(12)	

def numberSolution(n):
	'''all the digits of n are odd
	return the number of a such that a+reverse(a)= n'''
	sn = str(n)
	numberDigit = len(str(n))
	if numberDigit % 2 == 0:
		if sn[0] == '1':
			if numberDigit != 4 and numberDigit!=8: return 0
			elif numberDigit==4:
				if sn[1]!= sn[3]: return 0
				else: 
					return g(10+int(sn[1])) 
			elif numberDigit==8:
				if sn[1]!=sn[7] or sn[2]!=sn[6]	or sn[3]!= sn[5]:
					return 0
				return 	g(10 + int(sn[1])) * f(int(sn[2]) -1 ) * f(10 + int(sn[3]))	
		else:
			k = numberDigit/2
			for i in range(0,k):			
				if sn[i] != sn[numberDigit-1-i]:
					return 0
			s= g(int(sn[0]))
			for i in range(1,k):			
				s *= f(int(sn[i]))
			return s	
	else:
		return 0		
						
print numberSolution(1313), numberSolution(1111), numberSolution(3335), numberSolution(99)	

def generate(n):
	'''return the list of all numbers whose digits are odd and has n digits'''
	A=[1,3,5,7,9]
	if n ==1 :
		return A
	else:
		L = []
		T = generate(n-1)	
		for t in T:
			for a in A:
				s = str(a) + str(t)
				L.append(int(s))
		return L
# print generate(3), len(generate(3))				
def main()	:
	limit = 9

	s = 0
	for k in range(2,limit,2):
		sk = 0
		lk = generate(k)
		for x in lk:
			# if x < 2000 and numberSolution(x) > 0:
			if  numberSolution(x) > 0:
				# print x, numberSolution(x)
				sk+= numberSolution(x)
		print k,sk
		s+=sk		
	print 'answer',s
def test():
	k = 8
	l = generate(8)
	s1,s2 = 0,0
	for x in l:
		if str(x)[0] == '1' and numberSolution(x) > 0:
			s1+=numberSolution(x)
			# print x, numberSolution(x)
		elif str(x)[0] != '1' 	:
			s2+=numberSolution(x)
	print s1,s2		
main()		
# test()			