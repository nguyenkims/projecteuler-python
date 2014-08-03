# -*- coding: utf-8 -*-
import time as tm
import math as m

t1 = tm.time()*1000
f=open('base_exp.txt', 'r')
l=[i.strip().split(",")+[n+1] for (n,i) in enumerate(f.readlines())]
print l[0], l[1]

l = map(lambda i: (int(i[0]),int(i[1]), i[2]), l)
l = map(lambda (x,a,n): (a*m.log(x), n), l)
max = max(l)
t2 = tm.time()*1000

print max,t2-t1,'ms'