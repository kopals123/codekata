m=input().split()
n=int(m[1])
a=[int(k) for k in input().split()]
b=sorted(a)
c=b[::-1]
print(c[n-1])
