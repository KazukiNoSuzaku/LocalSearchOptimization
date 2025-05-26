import pandas as pa
from w2v_similar import ge
import numpy
from location import lo
from LocRem import rem
a= input()
b=a.split(' ')
for i in b:
	if i in rem():
		p=lo(a)
		b.remove(i)
d=[]
e=[]
for i in b:
	d.append(ge(i,'NOUN',.75))
for i in d:
	for it in i:
		e.append(it)
#print(e)
c=0
f2=[]
f=[]
for x in p:
	c=c+1
	match=[s for s in x.split(' ') if any(xs in s for xs in e)]
	if len(match) >0:
		f2.append(x)
		f.append(c)		
print(f2)
powe=[]
for x in p:
	c=0
	for i in range(0,len(b)):
		match=[s for s in x.split(' ') if any(xs in s for xs in d[i])]
		if len(match) <=0:
			c=1
			break
	if c==0:		
		powe.append(x)
#the powe would give us fields with both data and managers
#the original f2 list contains all job titles with relevant info. 