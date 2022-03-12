no=int(input())
sum1=0
a=no
t=0
for i in range(1,no):
	b=0
	sum1=a
	# for front space
	for j in range(no-i):
		print("0",end=" ")
	
	# for left side Triangle
	for j in range(i):
		print(sum1,end=" ")
		b=sum1
		sum1=a+b
		b=a
	#### for Right side Triangle
	if i==2:
		print(sum1,end="")
	elif i>2:
		t=0
		for j in range(i-1):
			print(sum1,end=" ")
			t=no-i+1
			sum1=sum1+t		
	
	a-=1
	##for spaces
	print(" 0"*(no-i))
# for last row
for i in range(1,no+5):
	print(i,end=" ")





	
	








