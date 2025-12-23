class Pattern:
    def fun1(self):
        for i in range (1,6):
            print("*"*i)
            print("\n--- Pattern ---")
        
class max_num:
    
        def find_max(n1,n2,n3,n4):
             if n1>n2 and n1>n3 and n1>n4:
               print("n1 is the greatest number")
    
             elif n2>n1 and n2>n3 and n2>n4:
              print("n2 is the greatest number")

             elif n3>n1 and n3>n2 and n3>n4:
              print("n3 is the greatest number")

             else:
              print("n4 is the greatest number")
              n1=int(input("Enter the 1 number: "))
              print("\n--- Find Maximum ---")
n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))
n3 = int(input("Enter 3rd number: "))
n4 = int(input("Enter 4th number: "))

class rev:
   def fun3():
    n =int(input("Enter Number :"))
    rem=0
    rev=0
    while(n!=0):
        rem = n % 10
        rev = rev*10+rem

        n//=10
    return rev
    
class middle_char:
   def print_middle_chars(self):
       if len(self)<3:
        return"It is too short"
 
       elif len(self) % 2 == 0:
        return "not this"
       else:
        mid = len(self) // 2
        return self[mid-1] + self[mid] + self[mid+1]


obj1 = Pattern()
obj2 = max_num()
obj3 = rev()
obj4 = middle_char()



obj1.fun1()


obj2.find_max(n1, n2, n3, n4)

print("\n--- Reverse Number ---")
num = int(input("Enter a number to reverse: "))
print("Reversed number:", obj3.fun3(num))

print("\n--- Middle Characters ---")
word = input("Enter a word: ")
print("Middle characters:", obj4.print_middle_chars(word))



