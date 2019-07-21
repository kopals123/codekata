a=int(input())
b=[int(k) for k in input().split()]
z=[]
for i in b:
    if(i<a):
        z.append(i)
print(*z)
