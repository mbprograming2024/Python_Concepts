# # 1 Write a  Python program to triple all numbers in a given list of integers. Use  Python map.

# def trimpler(x):
#     return x*3


# x = map(trimpler,[1,2,3,4,5,6,7,8,9])
# print(list(x))


# # 2. Write a Python program to add three given lists using  Python map and lambda.

# def adding(x,y,z):
#     return x+y+z

# a = [1,2,3]
# b = [4,5,6]
# c = [7,8,9]

# c = map(adding,a,b,c)
# print(list(c))

# # 3. Write a Python program to listify the list of given strings individually using Python map.

# def str_to_List(x):
#     list1 = []
#     for y in x:
#         list1.append(y)
#     return list1


# color = ['Red','Blue','Black','Yellow']

# x = map(str_to_List,color)


# print(list(x))  # [['R', 'e', 'd'], ['B', 'l', 'u', 'e'], ['B', 'l', 'a', 'c', 'k'], ['Y', 'e', 'l', 'l', 'o', 'w']]

# # 4. Write a Python program to create a list containing the power of said number in bases raised to the 
# # corresponding number in the index using Python map.

# def power(a,index):
#     return a**index

# a = [7,8,9,4,5,6]
# index = [1,2,3,4,6]

# x = map(power,a,index)

# print(list(x))


# # 5. Write a Python program to square the elements of a list using the map() function.
# def square(x):
#     return x**2

# b = [1,2,3,4,8]

# x = map(square,b)
# print(list(x))

# # 6. Write a Python program to convert all the characters into uppercase and lowercase and eliminate duplicate 
# # letters from a given sequence. Use the map() function.

# def convert_up_lo(x):
#     return x.upper(),x.lower()



# a = ['a','b','c','d','a','c']
# a = set(a)

# x = map(convert_up_lo,a)

# print(list(x))
 
# # 7. Write a  Python program to add two given lists and find the difference between them. Use the map() function.


# def add_sub(list1,list2):
#     return list1+list2,list1-list2

# list1=[15,23,14,26,28]
# list2=[87,63,22,45,15]

# x = map(add_sub,list1,list2)
# print(list(x))

# # 8. Write a  Python program to convert a given list of integers and a tuple of integers in a list of strings.

# def convertToStr(x):
#     return str(x)

# a = [10,20,50,40]
# b = (10,60,88,90)
# x = map(convertToStr,a)
# print(list(x))
# x = map(convertToStr,b)
# print(list(x))


# 9. Write a Python program to create a new list taking specific elements from a 
# tuple and convert a string value to an integer.

# def toInteger(x):
#     return int(x)

# a = ['10', '60', '88', '90']

# c = map(toInteger,a)
# print(list(c))


# 10. Write a Python program to compute the square of the first N Fibonacci numbers, 
# using the map function and generate a list of the numbers.

# def square1(x):
#     return x*x

# Fabonaci_num = [0,1,1,2,3,5,8,13,21,34,55]

# x = map(square1,Fabonaci_num)

# print(list(x))


# 11. Write a Python program to compute the sum of elements of an array of integers. Use the map() function.

# a = [0,1,1,2,3,5,8,13,21,34,55]
# sum = 0
# for x in a:
#     sum = sum + x

# print(sum)


# def add_list_element(i):
#     return i

# a = [0,1,1,2,3,5,8,13,21,34,55]
# x = map(add_list_element,a)
# print(sum(a))






# 12. Write a  Python program to find the ratio of positive numbers, 
# negative numbers and zeroes in an array of integers.

# n1 = 0
# n2 = 0
# n3 = 0

# def sort_ne_po_zero(x):
#     if x > 0:
#         n1 = n1 + x
#     elif x < 0:
#         n2 = n2 + x
#     else:
#         n3 = n3 + x
# a = [0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]

# c = len(a)

# print(n1/c , n2/c , n3/c)



# 13. Write a  Python program to count the same pair in two given lists. use map() function.
# count = 0
# def mappping(x,y):
#     global count
#     if x == y:
#         count +=1
#         return x,y

# nums1 = [1, 2, 3, 4, 5, 6, 7, 8]
# nums2 = [2, 2, 3, 1, 2, 6, 7, 9]

# Y = map(mappping,nums1,nums2)
# print(list(Y))
# print(count)


# # 14. Write a Python program to interleave two lists into another list randomly. Use the map() function.

# import random

# # Define a function named 'randomly_interleave' that takes two lists as input
# def randomly_interleave(nums1, nums2):
#     # Create a list of iterators using the 'iter' function for each input list
#     iterators = [iter(nums1)] * len(nums1) + [iter(nums2)] * len(nums2)
#     result = list(map(next, random.sample(iterators, len(nums1) + len(nums2))))
#     # Return the result
#     return result


# nums1 = [1, 2, 7, 8, 3, 7]
# nums2 = [4, 3, 8, 9, 4, 3, 8, 9]

# print(randomly_interleave(nums1, nums2))


# 15. Write a Python program to split a given dictionary of lists into list 
# of dictionaries using the map function.

# que = marks = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# ans = [{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, 
#  {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]


# def list_of_dicts(marks):
#     for key, value in marks.items():
#         for val in value:
#             print(val,key)


# marks = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# list_of_dicts(marks)


# # 16 Python: Convert a given list of strings into list of lists using map function
# # colors = ["Red", "Green", "Black", "Orange"]
# # Convert the said list of strings into list of lists:
# # [['R', 'e', 'd'], ['G', 'r', 'e', 'e', 'n'], ['B', 'l', 'a', 'c', 'k'], ['O', 'r', 'a', 'n', 'g', 'e']]

# def string_to_list(x):
#     list1=[]
#     for i in x:
#         list1.append(i)
#     return list1

# colors = ["Red", "Green", "Black", "Orange"]

# x = map(string_to_list,colors)
# print(list(x))


# # 17. Write a Python program to convert a given list of tuples to a list of strings using the map function.

# # Original list of tuples:
# # [('red', 'pink'), ('white', 'black'), ('orange', 'green')]

# # Convert the said list of tuples to a list of strings:
# # ['red pink', 'white black', 'orange green']


# def tuple_to_string(x):
#     str=''
#     for y in x:
#         str+=y
#         str+=" "
#     return str
# tuplelist =  [('red', 'pink'), ('white', 'black'), ('orange', 'green')]

# x = map(tuple_to_string,tuplelist)
# print(list(x))
