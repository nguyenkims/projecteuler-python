ROW=[]
ERROR, NOT_COMPLETED, OK = -1,0,1
S=set([1,2,3,4,5,6,7,8,9])

def fillROW():
	for i in range(9):
		ROW.append([])	
	f = file('sudoku.txt')
	
	for i in range(0,20):			s=f.readline()
	
	f.readline()	
	for i in range(0,9):
		s = f.readline().strip()
		for j in range(0,len(s)):
			ROW[i].append(int(s[j]))
fillROW()		

def getCol(row):
	'''update col if row is changed'''
	col = []
	for i in range(9):
		col.append([])
	for i in range(9):
		for j in range(9):
			col[i].append(row[j][i])
	return col		
	

def attack(row,m,n):
	'''return [# case filled corresponds to (m,n), the possible choices for (m,n)]
	'''
	if row[m][n] > 0:
		return [-1,None]
	col = getCol(row)			
	s = set(row[m]).union(set(col[n]))
	i,j = m/3, n/3
	for x in range(3*i, 3*i + 3):
		for y in range(3*j, 3*j+3):
			s.add(row[x][y])
	try:
		s.remove(0)
	except KeyError:
		pass
	# print m,n,s		
	return [len(s), S.difference(s)]
def isDistinct(pList):
	'''test if all elements of pList are different'''
	length = len(pList)
	for i in range(length-1):
		for j in range(i+1,length):
			if pList[i] == pList[j] and pList[i] > 0:
				return False
	return True

				
def check(row):
	'''test if all case are filled'''
	for i in range(9):
		if not isDistinct(row[i]):
			# print 'row',i,row[i]
			return ERROR
	col = getCol(row)
	for i in range(9):
		if not isDistinct(col[i]):
			# print 'col', i, col[i]
			return ERROR
	l = []		
	for m in range(3)		:
		for n in range(3):
			l = []
			for i in range(3*m, 3*m +2):
				for j in range(3*n, 3*n +2):
					l.append(row[i][j])
			if not isDistinct(l)		:
				# print 'square',m,n,l
				return ERROR				
	for i in range(9):
		for j in range(9):
			if row[i][j] == 0:
				# print 'not completed', i,j,row[i][j]
				return NOT_COMPLETED
	return OK		

print ROW,'check',check(ROW)

def legalAttack(row)		:
	'''return row filled if possible'''
	changes  = 0
	for m in range(9):
		for n in range(9):
			t = attack(row,m,n)
			if t[0] == 8:
				k = t[1].pop()
				row[m][n] = k
				# print 'legal', m,n,k
				changes +=1 
	return [row,changes]				

	
	
def cycleAttack(row):
	'''return row filled if possible'''
	nFound = 1
	while nFound > 0:
		t = legalAttack(row)
		row = t[0]
		nFound = t[1]	
	print row,'check',check(row)
	if check(row) != NOT_COMPLETED:	
		return [row,check(row)]
	else:
		x,y,rowBackUp = -1,-1,[]
		m,n,t = -1,-1, None
		while m < 8 and n < 8:
			m+=1
			n+=1
			t = attack(row,m,n)	
			rowBackUp = row
			if t[0] == 7:
				# print 't',t
				x,y = m,n
				break
		if x == -1 :
			print 'too difficult ...'		
			return [row,ERROR]
			
		print 'launch guess attack', x,y, t[1]
		row = guessAttack(row,x,y, t[1].pop())
		if cycleAttack(row)[1] == ERROR:
			print 'launch another attack', x,y,t[1]
			row = guessAttack(rowBackUp, m,n,t[1].pop())
			row = cycleAttack(row)[0]
			if check(row) != OK:
				return [row,ERROR]				
		return [row,ERROR]							
						
	
def guessAttack(row,m,n,val)		:
	'''replace row[m][n] by val'''
	row[m][n] = val
	print 'guess', m,n,val
	return row
			
def main()			:
	nFound = 1
	cycleAttack(ROW)
main()	

def test()	:
	nFound = 1
	while nFound > 0:
		nFound = cycleAttack()
		# print 'nfound',nFound
	# guessAttack()
	print row,check()
# test()	