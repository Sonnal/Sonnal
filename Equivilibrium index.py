
def result(list1): 
    tsum=sum(list1)
    lsum=0
    for i in range(1,len(list1)):
         lsum=lsum+list1[i-1]
         rsum=tsum-list1[i]-lsum
         print("index value is:",i,lsum,rsum)
         if(lsum==rsum):
             print("Index value is:",i)
        
list1=[1,2,1,1,1,1]
result(list1)