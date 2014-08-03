def isPandigital(pN):
	'''test if pN contains 1->9'''
	sN = str(pN)
	if len(sN) != 9: 
		return False
	for i in range(1,10)	:
		if sN.find(str(i)) == -1:
			return False
	return True
N = 10 ** 9	
limit = 200
def attackTail()			:
	'''return the list of fibonacci numbers that ends with a pandigital number'''
	a,b,count,t,found = 0,1,1,0,0
	l = []
	while True:
		count +=1
		if count % 1000 == 0:
			# print 'attack', count
			pass
		if count % 2 ==0	:
			a= (a+b) % N
			t =a 
		else:
			b = (b+a) % N
			t = b
		st = str(t)
		length = len(st)
		if 	isPandigital(st[(length-9):]):
			# print 'found', count
			l.append(count)
			found +=1
			if found == limit:
				print 'finish attack tail'
				return l
			# return
L = attackTail()
print L
def attackHead()		:
	'''run through all fibonacci numbers, stop only at position where 
	the tail is pandigital and check if the head is too'''
	a,b,count,t = 0,1,1,0
	while True:
		count +=1
		if count > L[len(L) - 1]:
			print 'can not found'
			return
			
		if count % 2 ==0	:
			a= a+b
			t =a 
		else:
			b = b+a
			t = b
		if count in L :
			st = str(t)
			length = len(st)			
			print 'testing ', count, st[:9]
			if 	isPandigital(st[:9]) :
				print 'found', count
				return
attackHead()			