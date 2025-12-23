class A:
    def fun1(self):
     print("Method1!!")

class B: 
   def fun1(self):
       super().fun1()
       print("Method2!!")

class C(B,A):
   def fun1(self):
      super().fun1()
      print("Methood3!!")

obj =C()
obj.fun1()