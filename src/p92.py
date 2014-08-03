N= 81 * 8 # f(n) for all n < M will be smaller than N
M= 10 ** 7
L=[] #contain (i, type) for i from 0 to N
	# there are 3 types: 
	# non-determined: 0
	# ends with 89:2 
	# ends with 1:1

def f(n)	:
	'''sum of square of digits of n'''
	sn=str(n)
	s=0
	for i in range(0,len(sn)):
		t=int(sn[i])
		s+= t*t
	return s
def isTypeOne(n):
	'''test if the chain of n ends at 1'''
	while True:
		if n== 1: return True
		if n==89: return False
		n= f(n)
def initialiseL():
	for i in range(0,N):
		L.append([i,0])
	L[0][1]=1
	L[1][1]=1
	L[89][1]=2
initialiseL()
print 'L is initialized'		

def fillL():
	for (a,statA) in L:
		if statA==0:
			t=a
			while True:
				if t < N:
					if L[t][1] == 0: t = f(t)
					else: 
						L[a][1] = L[t][1]
						break
				else: t = f(t)		
fillL()
print 'L is filled'

def main():
	s,a=0,0
	while a < M:
		if L[f(a)][1] == 2:		s+=1	
		# else: print a
		a+=1	
	print 'answer:',s	
main()
	