a=input()
k=[]
for i in a:
    if(a.count(i)==1):
        k.append(i)
print("".join(k))
