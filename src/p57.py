'''using formula:
x[n+1] = 2 * y[n] + x[n]
y[n+1] = x[n] + y[n] '''

x,y=1,1
limit= 1000
count, it =0,0
while True:
	it +=1
	t = x
	x = 2*y +x
	y = t+ y
	if len(str(x)) > len(str(y)):
		count +=1
		print it
	if it >	limit: break

print 'answer:', count		