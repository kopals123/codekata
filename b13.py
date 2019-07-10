z=int(input())
flag=0
for i in range(2,z//2):
    if(z%i==0):
        flag=1
if(flag==1):
    print("no")
else:
    print("yes")
