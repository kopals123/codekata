n=input()
b=[int(m) for m in input().split()]
c=sorted(b)
d=c[::-1]
g=""
for i in d:
    g=g+str(i)
if(g.count("0")==len(g)):
    print("0")
else:
    print(g)
