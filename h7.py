n=int(input())
z=[]
a=[int(k) for k in input().split()]
for i in range(0,len(a)):
    if((i%2 ==0) and(a[i]%2!=0)):
        z.append(str(a[i]))
    if((i%2!=0) and (a[i]%2==0)):
        z.append(str(a[i]))
print(" ".join(z))
