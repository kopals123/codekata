z=input()
b=['a', 'e', 'i','o','u']
c=[]
for i in z:
    if(i not in b):
        c.append(i)
print("".join(c[::-1]))
