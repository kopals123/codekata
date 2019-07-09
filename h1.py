n=input()
a=[int(z) for z in input().split()]
c=[]
for i in set(a):
    if(a.count(i)!=1):
        c.append(i)
print(*sorted(c))
