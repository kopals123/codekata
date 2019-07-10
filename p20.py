n=input()
k=[]
for i in n:
    k.append(chr(((d+3)%26)+ ord('a')))
print("".join(k))
