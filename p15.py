z=input()
c=[]
for i in set(z):
    c.append(z.count(i))
d=max(c)
for i in z:
    if(z.count(i)==d):
        print(i)
        break
