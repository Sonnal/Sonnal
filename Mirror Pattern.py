no=int(input())
for i in range(no,0,-1):
	print(" "*(no-i),end="")
	for j in range(i,-1,-1):
		print(j,end="")
	for j in range(1,i+1):
		print(j,end="")
	
	print()

print(" "*(no-1),"0")
##### Mirror Image
for i in range(0,no+1):
	print(" "*(no-i),end="")
	for j in range(i,-1,-1):
		print(j,end="")
	for j in range(1,i+1):
		print(j,end="")
	
	print()
	