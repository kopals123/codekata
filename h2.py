n=input()
b=[int(m) for m in input().split()]
c=sorted(b)
d=c[::-1]
g=""
for i in d:
    g=g+str(i)
print(g)
