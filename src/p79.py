def isCompatible(a,n):
	'''a = 317, b=531278 return true'''
	sa, sn = str(a), str(n)
	pos1=sn.find(sa[0])
	if pos1 < 0:return False
	for i in range(pos1+1,len(sn)-1):
		 if sn[i] == sa[1]:
			for j in range(i+1,len(sn)) :
				if sn[j] == sa[2]: return True
	return False

print isCompatible(317,531278)				
print isCompatible(317,753128)		

f = file("keylog.txt", "r")
L=[] #list all logins

t = f.next()

while True:
	try:
		L.append(t[0:3])
		t= f.next()
	except StopIteration:
		break	
print L	

def isOK(n):
	for x in L:
		if not isCompatible(x,n):
			return False
	return True		

n=10 ** 4	
while True:
	print n
	if isOK(n):
		print n
		break
	n += 1	