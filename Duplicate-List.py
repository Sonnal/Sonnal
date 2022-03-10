l=list(input().split(','))
res=[]
for i in l:
	if (l.count(i))>1:
		res.append(i)
print(*(set(res)))