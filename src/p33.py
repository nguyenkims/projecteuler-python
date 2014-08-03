def find_fraction():
	li=[]
	for a in range(1,10):
		for b in range(1,10):
			for c in range(1,10):
				ab= int(str(a)+str(b)) #ab
				ca= int(str(c)+str(a)) #ca
				bc=int(str(b)+str(c)) #bc
				if  ab!=bc and ab*c== bc*a:       #ab/bc=a/c 
					li.append((ab,bc))
				if  ab != ca and ab*c == ca ** b:  #ab/ca=b/c	
					li.append((ab,ca))
	print li
find_fraction()					