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
