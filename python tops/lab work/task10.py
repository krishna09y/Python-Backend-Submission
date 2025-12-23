class A:
    def fun1(self):
        l = [56, 27, 32, 41, 16]
        n = len(l)

       
        for i in range(n):
            min_element = i
            for j in range(i + 1, n):
                if l[j] < l[min_element]:
                    min_element = j

            
            l[i], l[min_element] = l[min_element], l[i]

        print("Sorted list:", l)


class B(A):
    def fun2(self):
        print("This")


# Create objects
objA = A()
objA.fun1()

objB = B()
objB.fun1()  # Inherited from A
objB.fun2()  # Own method