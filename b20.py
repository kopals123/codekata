z=int(input())
b=z*5
k=[]
if(z==0):
    print("0 0 0 0 0")
else:
    for i in range(1,b+1):
        if(int(i)%z==0):
            k.append(int(i))
    print(*k)
