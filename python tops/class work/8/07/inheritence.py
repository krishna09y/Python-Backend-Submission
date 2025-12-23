class A :
    def fun1(self):
        rows =6

        for i in range (rows):
            for j in range (rows - i - 1):
                print(" ",end="")
            for j in range (2 * i + 1):
                print("*",end="")
            print()
   
class B (A):
    

    def fun2(self, n):
        n = self.value
        sign = -1 if n < 0 else 1
        n = abs(n)
        reversed_n = 0
        while n > 0:
            reversed_n = reversed_n * 10 + n % 10
            n //= 10
        return sign * reversed_n
    
class C (B):
    def fun3(self):
        if len(self) < 3:
            return "It is too short"

        elif len(self) % 2 == 0:
            return "not this"
        else:
            mid = len(self) // 2
            return self[mid-1] + self[mid] + self[mid+1]
        
obj=C()
obj.fun1()
obj.fun2(12345)
obj.fun3()
