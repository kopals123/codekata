n=input()
m=input()
r=[]
q=[]
k=[]
for i in n:
    r.append(ord(i)-ord('a'))
for i in m:
    q.append(ord(i)-ord('a'))
for i,j in zip(r,q):
    k.append((chr((i+j)%26+ord('a')+1)))
print("".join(k))
