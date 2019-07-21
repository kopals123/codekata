a=input().split()
b=a[0]
c=a[1]
flag=0
d=input().split()
for i in d:
    if (i==c):
        flag=flag+1
print(flag)
