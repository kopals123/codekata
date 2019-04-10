a=[]
for i in range(0,3):
  ele=int(input())
  a.append(ele)
 b=a[0]
for i in a:
  if(i>b):
    b=i
 print(b)
