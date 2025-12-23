from packges import *

while True:
    menu = """
    press 1 
    press 2
    press 3
    press 4
    press 5 (Exit)
    """
    print(menu)

    choice = int(input("Enter Choice : "))

    if choice == 1:
        obj1.fun1()

    elif choice == 2:
        obj2.find_max(n1, n2, n3, n4)

    elif choice == 3:
        obj3.fun3()

    elif choice == 4:
        obj4.print_middle_chars()

    elif choice == 5:
        print("Exit")
        break

    else:
        print("Invalid process")
