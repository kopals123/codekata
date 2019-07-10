z=input().split()
a=int(z[0])
b=int(z[1])
k=[]
for i in range(a+1,b):
    if(i%2!=0):
        k.append(i)
print(*k)
