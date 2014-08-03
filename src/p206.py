import math

L=[] #contains about 100 intervals in which a*a must be
for i in range(0,10):
	a = int('1'+str(i)+'2') * 10 ** 14
	b= int('1'+str(i)+'3') * 10 ** 14
	ta,tb=int(math.sqrt(a)), int(math.sqrt(b))
	L.append([ta,ta*ta,tb,tb*tb])
# print L
s=0
for (a,sa,b,sb) in L:
	s+= (b-a)/5
print s	
	
def isOK(n):
	'''test if n = 1_2_3_4_5_6_7_8_9'''
	sn=str(n)
	for i in range(1,10):
		if sn[i*2-2]!= str(i): return False
	return True

minimum=int(math.sqrt(10**16))
maximum=int(math.sqrt(192*10 ** 14))
print minimum, maximum, (maximum-minimum)/5

def main():
	for (a,sa,b,sb) in L:
		print 'attack',a,b
		for i in range(a,b):
			s=str(i)
			if s[len(s)-1]=='3' or s[len(s)-1]=='7':
				if isOK(i*i) :
					print i,i*i
					break
	
main()