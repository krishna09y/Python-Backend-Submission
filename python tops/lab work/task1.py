num = int(input("Enter a number: "))

count=0
n = abs(num)  # To handle negative numbers
while n !=0:
    n //=10
    count+=1
    
    
print("Length of the number is :",count)



