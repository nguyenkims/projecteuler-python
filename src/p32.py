def is_ok(n):
	'''verify if n(string) contains distinct digits and does not contain 0'''
	if len(n) > 1:
		for i in range(0,len(n)-1):
			if n[i] == '0':
				return False
			for j in range(i+1, len(n)):
				if n[j] == '0':
					return False				
				# print i,j
				if n[i] == n[j] :
					# print i,j,n[i],n[j]
					return False
		return True
	else:
		return True
def is_pandigital(n):
	''' is_ok(n) and n contains 1->9'''		
	if not is_ok(n):
		return False
	for i in range(1,10)	:
		if  n.find(str(i)) == -1 :
			return False
	return True
			
def test()	:
	if is_ok("7438") and  not is_ok("624296"):
		print 'ok'
	else:
		print 'not ok'	
# test()

def main():
	
	a=[] # contains all pandigital numbers
	s=0 
					
	for i in range(100,1000):
		if is_ok(str(i)):
			for j in range(10,100):
				if is_ok(str(i)+str(j)) :
					t = i *j
					if is_pandigital(str(i)+str(j)+str(t)):
						print i,j,t
						if t not in a:
							a.append(t)
	for i in range(1000,10000):
		if is_ok(str(i)):
			for j in range(1,10):
				if is_ok(str(i)+str(j)) and len (str(i)+str(j)) == 5:
					t = i *j
					if is_pandigital(str(i)+str(j)+str(t)):
						print i,j,t
						if t not in a:
							a.append(t)						
	for i in a:
		s+=i
	print a						
	print 'answer=' ,s 					
main()						