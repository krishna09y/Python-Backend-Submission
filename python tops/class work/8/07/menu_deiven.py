# s= "Hello World"

# print(len(s))         #for string length
# print(s.capitalize())    # for capital first letter of string
# print(s.upper())          # it capital the whole string
# print(s.lower())          # is written in small letters
# print(s.center(18,"*"))   # it put the star or something else of centering the string
# print(s.endswith("ld"))   #it check end letters of strings
# print(s.find("e"))         #it find the word 
# print(s.isalnum())         #is check the string is alphabatical or numerical
# print(s.isalpha())         # is check the string is alphabatical
# print(s.replace("l","p"))  # it replace the word or letters
# print(s.count("o"))        # it counts the words
# print(s.swapcase())        #if the capital letter convert in small and small into capital
# print(s.title())

# s="Welcome to Python"
# print(len(s))

# print(s[])

# s = input("Enter Name : ")
 
 
# if len(s) % 2==0:
#  print("not this ")

# else:
#  mid=len(s)//2
#  print(s [mid-1]+s [mid]+s[mid+1])


def print_middle_chars(s):
 if len(s)<3:
  return"It is too short"
 
 elif len(s) % 2 == 0:
        return "not this"
 else:
        mid = len(s) // 2
        return s[mid-1] + s[mid] + s[mid+1]

s = input("Enter Name: ")
print(print_middle_chars(s))

