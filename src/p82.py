A=[]
limit = 10 ** 6
def fillA()			:
	B = []
	inp = file('matrix.txt')
	t = inp.readline()
	while t!="":
		# K = t.strip().split()
		K = t.strip().split(',')
		B.append(K)
		t = inp.readline()
	# print B
	for i in range(0,len(B)):
		A.append([])
	for b in B:
		for i in range(0,len(B)):
			A[i].append(int(b[i]))
	# print A	
	print len(A)	
fillA()
L= len(A)
print 'L=',L
def distance(m,i,n,j):
	'''return the distance from (m,i) to (n,j)
	note that m,n is the column number and i,j are row number'''
	if m > n: return -1
	elif m == n: 
		 #A[m][i] -> A[m][j]
		s = 0
		if i < j:
			for k in range(i,j+1): s+= A[m][k]
		else:
			for k in range(j,i+1): s+= A[m][k]
		return s
	elif m + 1 == n:	
		t1= A[m][i] + distance(n,i,n,j)
		t2=  distance(m,i,m,j) + A[n][j] 
		if t1< t2: return t1
		else: return t2
	else:
		minimum = limit
		middle = int((m+n)/2)
		for k in range(0,len(A[m]))		:
			s = distance(m,i,middle,k) + distance(middle,k,n,j) - A[middle][k]
			# print s,minimum,middle,k,distance(m,i,middle,k), distance(middle,k,n,j)
			if s < minimum:
				# print s,minimum,middle,k,distance(m,i,middle,k), distance(middle,k,n,j)
				minimum = s
		return minimum

def fillColumn(n):
	'''corresponding to each case in n th column, return the distance 
	from the first column '''
	l = []
	if n == 0:
		for i in range(0,L):
			l.append(A[0][i])
		return l
	else:
		l1 = fillColumn(n-1)
		for k in range(0,L)		:
			minimum = limit
			for i in range(0,L)		:
				t= l1[i] + distance (n-1,i,n,k) - A[n-1][i] 
				if t < minimum: minimum = t
			l.append(minimum)
		return l			
X= fillColumn(79)
print X, min(X)
