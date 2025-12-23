# n = lambda a,b,c,d : a+b+c+d 
# print(n(10,32,21,16))


# even_odd = lambda x:"Even" if x%2==0 else "odd"

# print(even_odd(10))
# print(even_odd)*

# l = [1, 2, 0, 1, 3, 0, 1, 0, 0, 1]
# l = sorted(l, key=lambda x: x == 0)
# print(l)

l = [1, 2, 0, 1, 3, 0, 1, 0, 0, 1]
n= len(l)
i=0
j = n-1
target = 0

for i in range(0,n):

    if l[i]==target:
        
        l[i],l[j]=l[j],l[i]

print(l)