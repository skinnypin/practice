# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly" ]

# mylist =[]


# for k in  range(len(list1)):
    
  
#     mylist.append(list1[k]+list2[k])
  
# numbers = [1, 2, 3, 4, 5, 6, 7]
# numberlist = []
# for num in numbers:
#     numberlist.append(num)
# print(numberlist)

# thislist = ["apple", "banana", "cherry"]
# if "mango" in thislist:
#     print("Yes")
# else:
#     print("no")


#program3 

# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# list2_len = len(list2) -1
# print(list2_len,'000000000000000')
# list3 = []
# for i in range (len(list1)):
#     print(list1[i] , list2[list2_len - i])


#program4
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

# Iterate over a copy of the list to avoid modifying it directly
for elem in list1:
    if len(elem) == 0:
        list1.remove(elem)

print(list1)

    
print(list1)

# if "" in list1[0:5]:
#     list1.remove("")
# print(list1)

