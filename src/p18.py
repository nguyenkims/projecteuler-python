line='abc'
data=[]

def get_right(da):
	return [x[1:] for x in da[1:]]

def get_left(da):
	return [x[:-1] for x in da[1:]]

def max_val(a,b):
	'''return a if a >b 
	b if not
	'''
	if a>b:
		return a
	else:
		return b
	

def find_max(da):
	'''find the max sum from top to button of da
	'''
	if len(da) == 0:
		return 0
	if len(da)==1:
		return int(da[0][0])
	else:
		max_left=find_max(get_left(da))
		max_right=find_max(get_right(da))
		return int(da[0][0]) + max_val( max_left, max_right )	
def populate():
        f = file("p18.txt")
	'''get data form p18.txt to data
	'''			
	global line
	while len(line) > 1 :
		line=f.readline()
                #print line
		a = line.strip('\n').split(' ')
		data.append(a);
		#print a

        
populate()
data = data[:-1]

print data
print '===================================='
#print get_left(data)

print '===================================='
#print get_right(data)


tmp=[['64'], ['47', '82']]
print '===================================='
print find_max(tmp)

print '===================================='
print find_max(data)


	
	
