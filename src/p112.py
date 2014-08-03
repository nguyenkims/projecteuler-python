limit=10 ** 4
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

print isIncreasingNumber(134468)	
print isDecreasingNumber(66420)	

n,s=1,0
while s==0 or 100*s >= n:
	if isIncreasingNumber(n) or isDecreasingNumber(n):
		# print n,s
		s+=1
	if n%100000 == 0:print n,s	
	n+=1
print 'found',n-1,s