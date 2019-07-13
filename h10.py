n=input()
a=input()
b=input()
for i in b:
    flag=0
    if( (i in a) and (a.count(i)==b.count(i))):
        flag=1
if(flag==1):
    print("YES")
else:
    print("NO")
