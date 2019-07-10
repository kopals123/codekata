z=input().split()
a=int(z[0])
b=int(z[1])

k=[]
def ams(n):
    sum=0
    for i in n:
        sum=sum+(int(i)**3)
    if(sum==int(n)):
        return True
for i in range(a,b):
    if(ams(str(i))==True):
        k.append(i)
print(*k)    
