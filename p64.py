a=input().split()
b=int(a[0])
c=int(a[1])
z=[]
d=[int(k) for k in input().split()]
for i in d:
    if(i<c):
        z.append(i)
f=sorted(z)
print(*f)
