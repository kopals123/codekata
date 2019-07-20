a=input().split()
b=int(a[0])
c=int(a[1])
flag=0
d=[int(k) for k in input().split()]
for i in range(len(d)):
    for j in range(1,len(d)):
        if((d[i]+d[j]==c)and(i!=j)):
            flag=1
            break
if(flag==1):
    print("yes")
else:
    print("no")
