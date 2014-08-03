import functions

limit =  10**6
def fac(n):
	'''return n!'''
	s=1
	for i in range(1,n+1): s*=i
	return s
print fac(5), 7*fac(9)	
FAC=[fac(i) for i in range(0,10)]
print FAC

def f(n):
	'''return the sum of factorial of digits of n'''
	sn,s = str(n),0
	for i in range(0,len(sn)):	
		s+= FAC[int(sn[i])]
	return s
print f(69),f(871)	

data=[] #contains (i,has i scanned)
def initializeData():
	for i in range(0,limit):
		data.append([i,False])
	data[0][1] = True
	print 'data is initialized'	


def test(n)	:
	l = []
	l.append(n)
	while f(n) not in l:
		l.append(f(n))
		n = f(n)
	print l
# test(69)	

def isOK(n):
	'''by ignoring the 0s at the ends of n
	test if digits of n are in an increasing order'''
	sn = str(n)
	k=len(sn) -1 
	while sn[k]=='0':
		k-=1
	t = sn[:(k+1)]	
 	return functions.isIncreasingNumber(int(sn[:(k+1)]))

def generateAnswer(n)		:
	'''this time, n is integer and the numbers starting with 0 will be eliminated
	'''
	l = functions.generateStrings(str(n))
	return [int(x) for x in l if x[0]!='0']
# print isOK(1052),isOK(15600)	

# print generateAnswer(123000), len(generateAnswer(123000))

def main():
	'''only search for the number whose digits are in an increasing order
	or have 0s at the end. Every time such a number is found, generate others from it digits by calling 
	generateAnswer'''
	n,s,passed,answer = 0,0,0,[]
	while n < limit -1 :		
		n+=1
		if not data[n][1] and isOK(n):
			l,t = [],n
			l.append(t)
			while f(t) not in l:
				l.append(f(t))
				if f(t) < limit:	data[f(t)][1] = True
				t = f(t)
			# print n,len(l),'l=',l	
			if len(l) == 60:
				print 'found',n,'s=',s
				answer+= generateAnswer(n)				
		else: 
			# print 'have passed',n	
			passed +=1
		if n %100000 == 0:	print 'attack',n
	print 'passed',passed, 'limit',limit
	print answer, len(answer)	
initializeData()	
main()	