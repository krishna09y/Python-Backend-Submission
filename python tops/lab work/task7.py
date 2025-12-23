# # l=[56,27,32,41,16]
# # n = len(l)

# # min_element = l[0]
# # for i in range (n):
# #     if l[i]<min_element:
# #         min_element = l[i]
# # print ("min number",min_element)

# #pallindrom
# n = int(input("Enter number:"))
# l=[]
# for i in range(n):
#     n1=int(input("Enter number:"))
#     l.append(n1)

# print(l)

# n3 =len(l)//2
# print(l[len(l)-1-i])
# ans ="Palidrome"
# for i in range (0,n3):
#     if l[i]==l[len(l)-1-i]:
#         continue
#     else:
#         ans = " not palindrome!!"
#         break

# print(ans)


# Selection sort
l = [56, 27, 32, 41, 16]

n = len(l)

for i in range(n):
    min_element = i
    for j in range(i + 1, n):
        if l[j] < l[min_element]:
            min_element = j
    # Swap
    l[i], l[min_element] = l[min_element], l[i]

print("Sorted list:", l)
