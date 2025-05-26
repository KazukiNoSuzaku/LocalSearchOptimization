import pandas as pd
def lo(a):
	r=pd.read_csv('data.csv')
	loc=r.joblocation_address.str.lower().str.replace(',',' ').str.replace('/',' ')
	title=r.jobtitle.str.lower().str.replace(',',' ').str.replace('/',' ')
	b=a.split(' ')
	h=0
	o=0
	send=[]
	for i in b:
		h=0
		i=str(i).lower()
		for j in loc:
			y=str(j).split(' ')	
			if i in y:
				send.append(title[h])
			h=h+1
	return(send)