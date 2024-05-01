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


