from itertools import permutations
z=permutations(input())
r=[]
for i in list(z):
    s="".join(list(i))
    if(s not in r):
        r.append(s)
for i in r:
    print(i)
