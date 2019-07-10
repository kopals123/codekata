n=input()
k=[]
for i in n:
    d=ord(i)-ord('a')
    k.append(chr(((d+3)%26)+ ord('a')))
print("".join(k))
