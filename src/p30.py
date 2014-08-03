limit=1

while limit * 9 ** 5 > 10 ** (limit-1) :
	limit += 1

N = 10 ** (limit-1)
print  'limit=%d  N=%d'% (limit,N)	


def f(n):
	'''return sum of fifth power of  digits of n'''
	s = 0
	for i in range(0,len(str(n))):
		s += int(str(n)[i]) ** 5 
	return s

def main():
	'''brute force'''
	s=0
	for i in range(2,N):
		if f(i) == i:
			print i
			s+=i
	print 'answer:',s		 

def main2():
	''' stocking f(i) in a[i]
	Better than main'''
	s=0
	a=[] # contains at position i f(i)
	for i in range(0,N)	:
		if i < 10:
			a.append(i ** 5)
		else:
			t = str(i)
			f = int(t[len(t)-1]) # last digit of i
			# print "%d:%d" %(i,f)
			a.append( f ** 5 + a[i/10])	
			if a[i] == i:
				s += i
				print i
	print 'answer:',s	

if __name__ == "__main__":
	main2()