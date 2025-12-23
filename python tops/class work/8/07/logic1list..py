
l=[]
ev=[]
od=[]
for i in range (1,31):
    l.append(i)

    if i%2==0:
        ev.append(i)

    else:
        od.append(i)


print(l)
print(ev)
print(od)

l=[73,34,106,24,78]

l.sort()

print("Smallest : ",l[0])
print("largest:",l[-1])
print("second largesrt : ",l[-2])

l=[1,2,3,1,2]

l1=[]

l2=[]
for i in l:
    if i not in l1:
        l1.append(i)
    else:
        l2.append(i)
print(l1)
print(l2)