def fib_gen(n):
	'''generate n first Fibonacci numbers'''
	a,b,i=0,1,1
	yield a,0
	yield b,1
	while i < n:
		i += 1
		if a > b:
			b = a+b
			yield b,i
		else:
			a = b +a	
			yield a,i
		
def test()		:
	t = fib_gen(10)
	for i in t:
		print i
# test()		

def final():
	k = 1000
	t = fib_gen(6*k)
	for i,j in t:
		if len(str(i)) > k:
			print k,j
			return
final()			