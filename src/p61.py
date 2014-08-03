limit = 10 ** 4
def f(k,n):
	'''if k==3 return triangle : n *(n+1) /2
	if k == 4: return square n*n ...'''
	if k==3:return n*(n+1)/2
	if k ==4: return n*n
	if k==5: return n*(3*n-1)/2
	if k==6: return n * (2*n-1)
	if k==7: return n * (5*n-3)/2
	if k==8: return n * (3*n-2)

P=[]	# P[3]:list of all triangle numbers smaller than limit
		# P[4]: squares numbers ....
for k in range(0,9):	
	P.append([])	
def fillP()		:
	for n in range(10,200):
		for k in range(3,9):
			if f(k,n) < limit and f(k,n) > 999:
				P[k].append(f(k,n))
fillP()				
print 'P is filled'
# print P[3]

def isCyclic(a,b):
	'''if a = xyzt and b = ztmn -> return true'''
	sa,sb=str(a),str(b)
	if sa[2] == sb[0] and sa[3] == sb[1]:
		return True
def generate(N, S):
	'''N=2, S=[a,b,c] return [ab,ba,ac,ca,bc,cb]'''
	if N==1:return S
	return [int(str(N+2)+str(x)) for x in generate(N-1)] + \
			[int(str(x) + str(N+2)) for x in generate(N-1)]
print generate(2)	 

def findTarget(N=3):
	'''find the set of N numbers that is cyclic and the first one is 
	triangle, the second is square and so forth'''		
	for a3 in P[3]:
		for a4 in [x for x in P[5] if isCyclic(a3,x)]:
			for a5 in [x for x in P[4] if isCyclic(a4,x) and isCyclic(x,a3)]:
				print a3,a4,a5
# findTarget()				

def test():
	a3 = 8128
	for a4 in [x for x in P[4] if isCyclic(a3,x)]:
		print a4
# test()		