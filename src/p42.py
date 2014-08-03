# -*- coding: utf-8 -*-
limit=40 
li=[] #list of triangle numbers

def fillLi():
	'''fills in li until limit'''
	for i in range(1,limit):
		li.append(i*(i+1)/2)
fillLi()
#print li

def f(s):
	'''return the sum of all letters of s
	ex: SKY-> 19+11+25=55'''
	t=0
	for i in range(0,len(s)):
		t+= int(ord(s[i])) - 64
	return t

print f('SKY')

fi=file("words.txt")
s=fi.readline()
liW=[ w[1:len(w)-1]  for w in s.split(",") ] #list of words from input file
#print liW

count =0
for w in liW:
	if f(w) in li:
		count +=1
		#print w, f(w)
print 'answer:',count		