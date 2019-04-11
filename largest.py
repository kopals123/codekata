a=[]
for i in range(0,3):
  ele=int(input())
  a.append(ele)
c=a[0]
for i in a:
  if(i>c):
    c=i
print(c)
