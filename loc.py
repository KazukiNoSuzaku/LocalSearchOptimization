import pandas as pd
#removing locations from job titles
r=pd.read_csv('data.csv')
title=r.jobtitle.str.lower().str.replace(',',' ').str.replace('/',' ')
loc=r.joblocation_address.str.lower().str.replace(',',' ').str.replace('/',' ')
ci=[]
d=0
for i in loc:
	try:
		y=i.split(' ')
		for j in y:
			if j in ci:
				d=d+1
			else:
				ci.append(j)
	except:
		d=d+1
ci=sorted(ci)
zen=[]
for x in title:
	try:
		yen=[]
		y=x.split(' ')
		for j in y:
			if j in ci:
				d=d+1
			else:
				yen.append(j)
		zen.append(yen)
	except:
		d=d+1
print(zen)						
