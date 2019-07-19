a=input()
flag=0
for i in a:
    if(a.count(i)==1):
        flag=1
    else:
        flag=0
        break
if(flag==1):
    print("Yes")
else:
    print("No")
