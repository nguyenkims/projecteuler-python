'''Using a property of pythagorean numbers:
if c^2 = a^2 + b^2 then exists m,n,k such that
c = (m^2+n^2)k
a = (m^2-n^2)k
b=2mnk 

and then p = 2m(m+n)k
By iterating m,n,k, we will find all (p,a,b,c)
'''
import math
limit = 1000
li=[] #contains all couple (p,c)

limitM=int (math.floor(math.sqrt(limit)))
for m in range(2,limitM):
	for n in range(1,m):
		t = 2*m*(m+n)
		
		limitK= limit/ t
		for k in range(1,limitK):
			a=(m*m - n*n) * k
			b = 2*m*n*k
			c=(m*m + n*n) * k
			p = t* k
			if (p,c) not in li:	
				li.append((p,c))

def f(p)			:
	'''the number of different right triangle with p as perimeter '''
	s=0
	for (a,b) in li:
		if a == p: 
			s+=1
			print p,b
	return s	


def main():
	m,P=-1,-1
	for p in range(1,limit):

		if p % 2 == 0 and f(p) >= m:
			m = f(p)
			# print m,p
			P=p
	print m,P

# print li		
main()
# print len(li)	
# print f(120)
# print f(720)