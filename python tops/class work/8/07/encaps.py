class Encaps:
    def fun1(self):
        a=10
        self.a=a
    def fun2(self):
        print(self.a)

obj=Encaps()
obj.fun1()
obj.fun2()