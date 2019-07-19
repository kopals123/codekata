a=input()
k=[]
if(len(a)<3):
    print(a[0])
else:
    k.append(a[0])
    k.append(a[3])
    print("".join(k))
