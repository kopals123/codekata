a=int(input())
k=[]
for i in range(1,a+1):
    if(i%2!=0)and (a%i==0):
        k.append(i)
print(*k)
