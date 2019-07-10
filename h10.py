a=(input())
b=(input())
c=input()
flag=0
for i in c:
    if i in b:
        flag=1
if(flag==1):
    print("YES")
else:
    print("NO")
