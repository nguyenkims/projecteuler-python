import math
import functions

D=12000

def main():
	s=0
	for a in range(2,D/2+1):
		for b in range(2*a+1,min(3*a,D+1)):
			if functions.gcd(a,b) == 1:
				# print 'add:',a,b
				s+=1
			# else:	print 'delete',a,b	
	print 'answer:',s

main()
	