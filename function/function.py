# A function is block o code wich only runs when it is called
# you can pass parameter to function
# function car retun data as a result

# syntax
# def function_name():
#     print("Hello this is syntax for define the function")
#
# #here you call the function
# function_name()

# # example 2 : you can pass the parameter to function
# def parameterfun(name):
#     print("hello",name)
#
# parameterfun("mayur")


# # example : 3 you can also return value from function
# def parameter_retunr():
#     return "mayur"
# print("HEllo",parameter_retunr())


# # A parameter is the variable listed inside the parentheses in the function definition.
# def fun2(x):            # x is called parameter
#     pass

# An argument is the value that is sent to the function when it is called.
# fun2(50)    # 50 is called argument


# # Arbitrary Arguments, *args
# # you don’t know how many argument pass to the function then put * infront of parameter
# def fun4(*par):
#     for x in par:
#         print(x)
# fun4(2,4,5,6)

# # Keyword Arguments
# # we can pass the dictionary to the function
# def fun5(child1,child2,child3):
#     print(child1)
# fun5(child1="A",child2="B",child3="c")

# # Arbitrary Keyword Arguments, **
# def fun5(**child):
#     print(child["child1"])
# fun5(child1="A",child2="B",child3="c")

# # Default Parameter Value
# def fun6(name = "mayur"):
#     print("Hello",name)
#
# fun6()
# fun6("rushikesh")



# list1 = [1,2,3,4,5]
# tup1=(1,2,3,4,5)
# set1 = {1,2,3,4,5}
# def fun7(l):
#     for x in l:
#         print(x,end=" ")
#     print()
#
# fun7(list1)
# fun7(tup1)
# fun7(set1)
#
#
# dic = {"name":"mayur","last":"baviskar"}
# def fun7(l):
#     for x in l.items():
#         print(x,end=" ")
#     print()
# fun7(dic)

# # pass keyword
# # to define the empty function
# def fun8():
#     pass

# recurtion
# when function call itself again and again







