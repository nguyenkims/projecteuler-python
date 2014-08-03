

def fac(n):
	'''return n!'''
	if n==0:
		return 1
	else:
		return n * fac(n-1)
		
def getSubList(n,da):
	''' returns the sub list of data correspond to the number at n th position
	if data = da 
	We begin to count at n = 0
	'''
	length=	len (da)
	if length==1:
		if n==0:
			return da
		else:
			return []
	else:
		answer=[]	# contains the final answer
		#determines the first member of sublist
		tmp = fac(length-1)		
		firstPos= int (n / tmp)
		n1 = int (n % tmp)
		# print 'n1=', n1
		# print 'firstPos=', firstPos
 		
		cutList = da[0:firstPos] + da [(firstPos+1):]
		# print 'cutList=', cutList
		
		answer.append(da[firstPos])
		# print 'answer=', answer

		answer += getSubList(n1,cutList)
		return answer
	
def test():
	data=[0,1,2,3,4,5,6,7,8,9]
	pos=1000000
	ans=getSubList(pos -1 ,data)
	
	# print answer in number form
	s=""
	for i in ans:
		s+= str(i)
	print s

test()	
