z=int(input())
p=input()
a=p.split()
c=[]
for i in set(a):
    c.append(a.count(i))
d=min(c)
for i in a:
    if(a.count(i)==d):
        print(i)
        break
