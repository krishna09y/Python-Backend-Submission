# try:
#     n=int(input("Enter Number1:"))
#     n1=int(input("Enter Number2:"))

#     print("Addition :",n+n1)
# except ValueError as e:
#     print(e)
# else:
#     print("Try excuted!!")
# finally:
#     print("Finally executed!!")

# try:
#     n=int(input("Enter number1:"))
#     n1=int(input("Enter Number2:"))

#     print("Division :",n/n1)

# except ValueError as e:
#     print(e)

# except ZeroDivisionError as e:
#     print(e)



try:
    l =[56,27,45,32,54]

    n1=int(input("Enter Number2:"))
    print("Value of index : ",l[n1])

except Exception as e:
    print(e)
    print("Invalid ")