a=input()
b=[int(k) for k in input().split()]
c=[int(k) for k in input().split()]
z=[]
for i in b:
    if(i in c):
        z.append(i)
f=sorted(set(z))
print(*f)
