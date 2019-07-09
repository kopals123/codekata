from itertools import permutations
z=permutations(input())
for i in list(z):
    print("".join(list(i)))    
