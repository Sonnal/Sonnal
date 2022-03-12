no=int(input())
a=(abs(no//2))+1


for i in range(1,no+1):
	for j in range(1,no+1):
		if  i==a or (j==1 and i<a) or(j==a)or (i==1 and j>a) or(i==no and j<a) or(j==no and i>a):
			print("*",end ="")
		else:
			print(" ",end="")
	
	
	print()

	
	








