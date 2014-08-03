li=[] #contain 0! , 1!,....
limit=101
M= 10 ** 6
def populate(n):
	'''populate li until n! '''
	if n==0:li.append (1)
	else:
		populate(n-1)
		li.append(n*li[n-1])

populate(limit)
print 'finished populating li'
# print li
def C(n,i):
	'''return n!/(n-i)! * i*'''
	return li[n] / (li[i]*li[n-i])

count =0
for n in range(10,limit)	:
	for i in range(1,n):
		if C(n,i) > M:
			count +=1
			print n,i
print 'answer:',count			


	