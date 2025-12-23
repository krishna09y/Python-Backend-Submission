# #Patten
#  for  i in range(1,6):
#      for j in range(1,i+1):
#          print("*", end="")

#          print()

# for  i in range(1,6):
#     print("*"*i)

# for i in range(1,6):
#     for k in range(1,6-1):
#         print(" ", end="")
#     for j in range(1,i+1):
#         print("*",end="")

#     print()

# for i in range(1, 6):
#     print(" " * (6-i) + "*" * i)
# for i in range(5,0,-1):
#     print(" "* (5-i) + " *" * i)

#     for i in range (5,0,-1):
#         for k in range(1,5-1):
#             print(" ",end="")
#     for j in range(5,i-1,-1):
#             print(" *",end="")
#     print()  

#n=65

# for i in range(1,6):
#     print(chr(n)*i)

# for i in range (1,6): #row
#     for j in range (1,i+1): # coll0um
#         print(chr(n), end="")
#         n+=1
#     print()

# n = 65
# for i in range(1, 6):
#     print(*[chr(n + j) for j in range(i)])
#     n += i