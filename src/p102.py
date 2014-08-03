limit = 10 ** 4
def isOK(a1,a2,a3,m):
	'''test if m is in the same plan as a3 vis-a-vis to a1a2'''
	x1, y1= float(a1[0]), float(a1[1])
	x2,y2= float(a2[0]), float(a2[1])
	x3,y3=float(a3[0]), float(a3[1])
	x,y=float(m[0]), float(m[1])
	
	t =  (x-x1) * (y2-y1) - (y-y1) * (x2-x1)
	k = (x3-x1) * (y2-y1) - (y3-y1) * (x2-x1)
	if t*k > 0:
		return True
	return False
		
def isInterior(a1,a2,a3,m)	:
	'''test if m is in the triangle formed by a,b,c
	'''
	if isOK(a1,a2,a3,m) and isOK(a2,a3,a1,m) and isOK(a3,a1,a2,m):
		return True
def test():
	a1 =(-340,495)
	a2= (-153,-910)
	a3 = (835,-947)
	X= (-175,41)
	Y= (-421,-714)
	Z = (574,-645)
	m = (0,0)
	print 	isInterior(a1,a2,a3,m), isInterior(X,Y,Z,m)
	print intersection(X,m,Y,Z)
# test()	

def main():
	inp= file('triangles.txt')
	count = 0
	O = [0,0]
	TRI= []
	t = inp.readline()
	while (t!=""):
		l= t.strip().split(',')
		x = [int(l[0]), int(l[1])]
		y = [int(l[2]), int(l[3])]
		z = [int(l[4]), int(l[5])] 
		if isInterior(x,y,z,O): 
			count +=1
			# print x,y,z
		# else: count+=1	
		t = inp.readline()
	print 'count', count	
main()
	