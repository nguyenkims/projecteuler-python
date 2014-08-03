def isEgal(A,B):
	'''compare 2 lists A and B'''
	for a in A:
		if a not in B:
			return False
	return True
			
A = [i for i in range(1,7)]
S = 9
maximum = -1
for a1 in A:
	for a2 in A:
		for a3 in A:
			if a1+a2+a3 == 6:
				x1 = S - a1 - a2
				x2 = S - a2 - a3
				x3 = S - a3 - a1
				z1 = str(x1) + str(a1) + str(a2)
				z2 = str(x2) + str(a2) + str(a3)
				z3 = str(x3) + str(a3) + str(a1)
				L = [a1,a2,a3,x1,x2,x3]   
				if isEgal(A,L):
					print x1,x2,x3
					t =  max(int(z1), int(z2), int(z3))
					if t > maximum:
						maximum = t
print 'maximum', maximum						