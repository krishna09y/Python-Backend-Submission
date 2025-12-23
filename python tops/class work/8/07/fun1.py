def pattern1():
    n=65
    for i in range (1,6): #row
     for j in range (1,i+1): # coll0um
         print(chr(n), end="")
         n+=1
     print()

def pattern2():
   for  i in range(1,6):
     print("*"*i)

def pattern3():
   for i in range(5,0,-1):
     print(" "* (5-i) + " *" * i)

def pattern4():
   n=65
   for i in range(1,6):
    print(chr(n)*i)


pattern1()
pattern2()
pattern3()
pattern4()
   
