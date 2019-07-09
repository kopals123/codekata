n=input()
a=[int(k) for k in input().split()]
for i in a:
    if(a.count(i)!=1):
        break
print(i)
