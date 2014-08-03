import math

def gcd(a,b):
	'''return the greatest common divisor of a and b '''
	a,b=abs(a),abs(b)
	while a > 0 and b >0:
		if a>b:			a=a%b
		else:			b=b%a
	if a==0 and b>0:return b
	if b==0 and a>0:return a
	if a==0 and b==0: return 1

def isPrime(n):
	if n<2 : return False
	if n==2 : return True
	if n%2 ==0 :return False
	t = int(math.sqrt(n))
	#print n,t
	for i in range(2,t+1):
		if n % i == 0:
			#print i,n
			return False
	return True
def isIncreasingNumber(a):
	sa=str(a)
	for i in range(0,len(sa)-1):
		if int(sa[i]) > int(sa[i+1]):return False
	return True
def isDecreasingNumber(a):
	sa=str(a)
	for i in range(0,len(sa)-1):
		if int(sa[i]) < int(sa[i+1]):return False
	return True

def isPermutation(a,b):
	'''return true if digits of a are permutations of b'''
	sa,sb= str(a), str(b)
	for i in range(0,len(sa)):
		if sa.count (sa[i]) != sb.count(sa[i]): return False
	for i in range(0,len(sb)):
		if sa.count (sb[i]) != sb.count(sb[i]): return False	
	return True
	
def generateStrings(n)	:
	'''return the list of a where letters of a is combination of n
	ex:if n = 102, return [012,021,102,120,201,210]'''
	sn,l= str(n),[]
	if len(sn) == 1: return [n]
	else:
		for i in range(0,len(sn)):
			t =  sn[:i]+sn[(i+1):]
			# print 't=',t
			for x in generateStrings(t):
				y = sn[i]+str(x)
				# print 'y=',y
				if y not in l and len(str(y))== len(sn):
				 	l.append(y)
		return l	

limit = 10 ** 4
def intersection(a1,a2,a3,a4):
	'''returns the coordination of intersection of a1a2 and a3a4
	where a1 is the point at (x1,y1), a2 at (x2,y2) and so on'''
	x1, y1= float(a1[0]), float(a1[1])
	x2,y2= float(a2[0]), float(a2[1])
	x3,y3=float(a3[0]), float(a3[1])
	x4,y4=float(a4[0]), float(a4[1])

	denominatorX = (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)
	nominatorX = (x4-x2)*(y3-y4) - (y4-y2)*(x3-x4)
	if denominatorX != 0:
		alpha = nominatorX/ denominatorX

		# print nominatorX, denominatorX	
		# print a1,a2,a3,a4,alpha		
		x = alpha * x1 + (1-alpha)*x2
		y = alpha * y1 + (1-alpha) * y2
		return [x,y]
	else:
		return [limit,limit]		

def continuedFraction(pN,pLimit):
	'''return the pLimit terms of continued fraction of square root of pN'''
	listA, listB = [], []
	sRoot = int(math.floor(math.sqrt(pN)))
	sRest = pN - sRoot * sRoot
	listA.append(sRoot)
	x = int(2*sRoot/sRest)
	lNume = sRoot - x * sRest
	listB.append([x,lNume,sRest])
	# print listA,listB
	count = -1
	while count < pLimit-2:
		count +=1
		listA.append(listB[count][0])
		x = listB[count][1]
		y = listB[count][2]
		t = (pN-x*x)/y
		b0 = (sRoot-x)/t
		b1 = x*(-1)-b0 * t
		b2 = t
		listB.append([b0,b1,b2])
	return listA		
	
def test()		:
	print gcd(10,15), gcd(12,19), gcd(1001*8439943,1001*8439947)

if __name__=="__main__"	:
	test()	