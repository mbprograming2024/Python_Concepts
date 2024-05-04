# var_list=[1,2,3,4,5]
# print(var_list)

# # we can access list item using index
# print(var_list[1])

# # add item usign append() method
# # list allow duplicate
# var_list.append(1)
# print(var_list)

# # remove item from list
# var_list.remove(2)
# print(var_list)

# # type() and len()
# var_list1 = ["mayur",1,True,"kiran"]
# print(len(var_list1))
# print(type(var_list1))

# var_list3=[1,2,3,4,5]
# print(var_list3[1])
# print(var_list3[-1])
# print(var_list3[:3])
# print(var_list3[1:])

# # insert() method add element at specified location
# var_list3=[1,2,3,4,5]
# print(var_list3)
# var_list3.insert(2,60)
# print(var_list3)

# # add two list
# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)

# loop through the list
var_list5 = [1,2,3,4,5,6,7,8,9]

# loop using for loop
# for x in var_list5:
#     print(x)
#
#
# # while loop
# i = 0
# while i < len(var_list5):
#     print(var_list5[i])
#     i = i+1

# # using list comprihasion
# [print(x) for x in var_list5]

# # using range
# for x in range(len(var_list5)):
#     print(var_list5[x])

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
#
# newlist = [x for x in fruits if "a" in x]
# print(newlist)


# sorting list
# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort()
# print(thislist)


# sorting a list without using sort method
# var_list = [50,-6,-25,30,5,36]
# new_list = []
#
# while var_list:
#     min = var_list[0]
#     for x in var_list:
#         if x < min:
#             min = x
#     new_list.append(min)
#     var_list.remove(min)
#
# print(new_list)


# # everse a list
# var_list6 = [10,80,26,4,6,30,40]
# var_list6.sort()
# print(var_list6)
#
# for x in range(len(var_list6)-1,-1,-1):
#     print(var_list6[x],end=" ")


# a = ["a","A","b","C"]
# a.sort()
# print(a)

a = ["a","A","b","C"]
new_list = []
while a:
    min=a[0]
    for x in a:
        if ord(x) < ord(min):
            min = x
    new_list.append(min)
    a.remove(min)
print(new_list)

