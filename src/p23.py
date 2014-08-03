import math
LIMIT=8
# LIMIT=300
pTable=[] #contains all primes smaller than LIMIT
abundantTable=[] #contains all abundant numbers than LIMIT

def is_prime(n):
	'''return True if n is prime
	False if not
	'''
	root= int (math.floor(math.sqrt(n)))
	for i in range(2,root+1):
		if n % i == 0:
			return False;
	return True # n is prime

def fills_pTable():
	'''fills pTable
	'''
	pTable.append(2)
	pTable.append(3)
	tmp = int (math.floor(math.sqrt(LIMIT)))
	for i in range(5,tmp+1):
		if is_prime(i):
			pTable.append(i)

fills_pTable()
print pTable
	
def first_divisor(n):
	'''returns the first (smallest) divisor of n
	'''
	root=math.floor(math.sqrt(n))
	for i in range (0, len(pTable) ):
		if pTable[i] <= root and n % pTable[i] == 0:
			return pTable[i]
	return n # n is prime

def max_power(n,p):
	'''return k such that p^k | n and not for k+1
	'''			
	if (n % p != 0):
		return 0
	return 1 + max_power(n/p,p)	
	
def sum_divisor(n):
	'''return the sum of all divisors of n (except n)
	'''
	if  n ==1:
		return 0
	if n in pTable:
		return 1
	p = first_divisor(n)
	k = max_power(n,p)
	t = n / pow(p,k)
	
	s = 0
	for i in range(0,k+1):
		s+= pow(p,i)		
	return (sum_divisor(t)+t) * s - n	

print sum_divisor(2)	
print sum_divisor(4)	
print sum_divisor(12)	

def fills_abundant_numbers():
	'''fills abundantTable
	'''
	for i in range(11,LIMIT+1):
		if sum_divisor(i) > i :
			abundantTable.append(i)

fills_abundant_numbers()	
# print abundantTable
print 'abundantTable len:', len(abundantTable)
# for i in range (0,len(abundantTable)):
# 	if abundantTable[i] % 2 == 1:
# 		print "odd existed!", abundantTable[i]
	
def can_be_written_as_the_sum_of_2_abundant(n):
	'''return True if a number can be written as the sum of 2 abundant numbers
	'''		
	for i in range(0,len(abundantTable)):
		if abundantTable[i] < n:
			k = n - abundantTable[i]
			if k in abundantTable:
				return True
	return False		

can_be_written=[24] # contains all numbers that can be written as sum of 2 abundant
def addTo(a):
	''' add a to array can_be_written intelligently
	'''
	global can_be_written
	t1=[]
	t1.append(a)
	
	if can_be_written[0] > a:
		can_be_written = t1 + can_be_written
		return
	elif can_be_written[0] == a:
		return
	else:	
		for i in range(1,len(can_be_written)):
			if can_be_written[i] == a:
				return
			if can_be_written[i] > a:
				smaller= can_be_written[0:i]
				bigger=can_be_written[i:] 
				can_be_written = smaller + t1 + bigger
				return
		can_be_written = can_be_written + t1		

def fills_can_be_written():
	for i in abundantTable:
		for j in abundantTable:
			addTo(i+j)
# fills_can_be_written() #takes a lot of time			
# print can_be_written

total=[i for i in range(1,LIMIT+1)]
total.remove(1)
print total

def final():
	S = 0
	for i in range(1,LIMIT ):
		# if  not can_be_written_as_the_sum_of_2_abundant(i):
		if i not in can_be_written:
			S += i
			# print 'not abundant:',i

	print 'final sum:',S	
# final()		
if can_be_written_as_the_sum_of_2_abundant(LIMIT):
	print 'LIMIT can be written'		