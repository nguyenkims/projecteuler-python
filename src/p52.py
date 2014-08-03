def isPermutation(a,b):
	'''return true if digits of a are permutations of b'''
	sa,sb= str(a), str(b)
	for i in range(0,len(sa)):
		if sa.count (sa[i]) != sb.count(sa[i]): return False
	for i in range(0,len(sb)):
		if sa.count (sb[i]) != sb.count(sb[i]): return False
	
	return True

x = 1
while True:
	if isPermutation(x,2*x) and isPermutation(x,3*x) :
		if isPermutation(x,4*x) and isPermutation(x,5*x) and isPermutation(x,6*x) :
			print x
			break
	else:
		x+=1 		