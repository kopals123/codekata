a=input()
b=input().split()
k=[]
for i in b:
    k.append(b.count(i))
print(max(k))
