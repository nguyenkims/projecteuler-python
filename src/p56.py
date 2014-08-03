def generate(n,k):
	'''return list of n**i from i=0 to k-1'''
	l,i=[],0
	while i < k :
		if i==0:l.append(1)
		else: l.append(l[i-1] * n)	
		i+=1
	return l
print generate(10,10)		

limit=100
data=[]	#data[i]: generate(i,limit)
for i in range(0,limit):
	data.append(generate(i,limit))
print 'finish generating data'	

def sum_digit(n):
	s = str(n)
	t=0
	for i in range(0,len(s)): t+= int(s[i])
	return t
# print sum_digit(1234)	


def main():
	da=[] # contains list of (x,y, sum_digit(x**y))
	#need to create da because the direct calculation doesnot work

	m=-1 #max of sum of digits

	for i in range(0,len(data)):
		for j in range(0,len(data[i])):
			t=data[i][j]
			da.append((i,j,sum_digit(t)))		
	print 'finish populating da'		
	
	for (i,j,t) in da:
		if t >= m: 
			m=t
			print i,j,t
	print 'answer:',m			

main()