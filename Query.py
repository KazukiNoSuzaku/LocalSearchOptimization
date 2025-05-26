from w2v_similar import ge
import numpy
import pandas as pd
def valid():
	a= input()
	b=a.split(' ')
	d=[]
	e=[]
	for i in b:
		d.append(ge(i,'NOUN',.75))
	for i in d:
		for it in i:
			e.append(it)
	#print(e)
	p=pd.read_csv('data.csv')
	p=p.jobtitle.str.lower()
	c=0
	f2=[]
	f=[]
	for x in p:
		c=c+1
		match=[s for s in x.split(' ') if any(xs in s for xs in e)]
		if len(match) >0:
			f2.append(x)
			f.append(c)		

	## First set of jobs found should have all the words searched
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
	print(powe)
	# Search for data and managers seperately
	for i in range(0,len(b)):
		print(b[i])
		u=[]
		for x in p:
			match=[s for s in x.split(' ') if any(xs in s for xs in d[i])]
			if len(match) >0:
				u.append(x)
			#print(u)
			