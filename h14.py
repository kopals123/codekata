z=input()
a=[]
for i in z:
    a.append(i)
for i in a:
    for j in a:
        for k in a:
            if(i!=j)and (j!=k)and (k!=i):
                print(i+j+k)
            
    
