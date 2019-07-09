n=input()
b=[int(m) for m in input().split()]
d=[]
for i in set(b):
    if(b.count(i)!=1):
        d.append(i)
print(*sorted(d))
