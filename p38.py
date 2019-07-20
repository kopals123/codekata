a=int(input())
k=[]
for i in range(2,a+1):
    if(a%i==0)and(i%2==0):
        k.append(i)
print(*k)
