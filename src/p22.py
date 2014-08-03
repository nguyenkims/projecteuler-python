import os

inp="p22.txt" #initial input
out="p22_cleaned.txt" #input after replacing ',' by '\n'
sor="p22_sorted.txt" # sorted (alphebetically) using sort command of


def initialisation():
	'''initialise sor
	'''
	f=file (inp,"r")
	content = f.readline()

	f.close()

	# print content
	name=content.split(',')
	# print name[0]

	f=file(out,"w")
	for i in range (0,len(name)):
		f.write(name[i]+"\n")
	f.close()

	command = "sort " + out + " > " + sor
	os.system(command)

def alphe_sum(a):
	'''return sum of all characters of a
	ex: COLIN -> 3 + 15 + 12 + 9 + 14 = 53
	'''
	s=0
	for i in range(0, len(a)):
		tmp = 0
		if a[i] <= "Z" and a[i] >="A":
			tmp = ord(a[i]) - 64
		else:
			tmp=0
		# print a[i] + ": " + str(tmp)
		s += tmp
	return s;

# print "alphe sum:",alphe_sum("\"AARON\"")
# print "alphe sum:",alphe_sum("AARON")

if __name__== "__main__":
	initialisation()

	S=0
	f = file (sor)
	count =1
	while True:
		content = f.readline()
		if content!="":
			# print content
			S = S + alphe_sum(content) * count
			count = count + 1
		else:
			break
	f.close()
	print "total sum:", S