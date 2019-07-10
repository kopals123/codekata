k=[int(s) for s in input().split()]
l=k[0]
m=k[1]
p=l*m
while(l%m!=0):
    r=l%m
    l=m
    m=r
print(p//m)  
