a=input()
k=[]
for i in a:
    if(i.islower()==True):
        k.append(i.upper())
    else:
        k.append(i.lower())
print("".join(k))
