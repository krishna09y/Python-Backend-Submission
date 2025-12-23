# # file = open("test2.txt","W")
# # file.write("write method!!")
# # file.close()

# l = []

# for i in range(1,31):
#     l.append(i)

# l1 = str(l)

# file = open("Test3.txt","w")
# file.write(l1)
# file.close()


# file = open("Test4.txt","w+")
# file.write("hello w+ method!!")
# print(file.tell())
# file.seek(0)
# print(file.read())
# file.close()

# file = open("Test3.txt","r+")
# print(file.read())

# file.write("hello r+ world")
# file.close()


file = open("Test3.txt","a+")


file.write("hello a+ world")
file.close()
