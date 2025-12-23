class Myclass1:

    def pattern1(self):

        for i in range(1,6):
            print("*"*i)

    def pattern2(self):
        
        for i in range(1,6):
            print(" "*(6-i),"*"*i)

    def pattern3(self):
        for i in range(1,6):
            print(" "*(6-i)," *"*i)


class Myclass2:
    
     def list1():
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

     def list2():
        

        l=[73,34,106,24,78]

        l.sort()

        print("Smallest : ",l[0])
        print("largest:",l[-1])
        print("second largesrt : ",l[-2])

