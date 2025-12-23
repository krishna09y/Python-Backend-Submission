def decorator(func):
    def wrapper():
        print("Before calling the function.")
        func()
        print("After Calling the function.")
        return wrapper
    

@decorator#Appying the decorator to a function 
def greet():
    print("Hello,World!")
greet()