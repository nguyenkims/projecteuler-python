def f(l):
	'''return a/b corresponding to list l'''
	if len(l) == 1:
		return [l[0],1]
	else:
		l1=l[1:]	
		a=f(l1)
		# print a,l1
		return [l[0]*a[0] + a[1], a[0]]
l=[1,2,2]
print f(l)		

L=[] # corresponding to representant of e

def fillL():
	k, count = 0,1
	while k < 100:
		if k==0:L.append(2)
		elif k % 3 == 2:
			L.append(2*count)
			count+=1
		else:	
			L.append(1)
		k+=1
fillL()

print f(L[:10])	
def main():
	a = f(L[:100])
	sa = str(a[0])
	s=0
	for i in range(0,len(sa)):
		s+= int(sa[i])
	print 's=',s
main()		