# tuple_items = [10,20,30,40,50,60]
#
# # to print all tuple
# print(tuple_items)
#
# # to access specific value in tuple

# tuple_items = [   10  ,   20  ,   30  ,   40  ,   50     ,    60]
#                   0       1       2       3       4           5
#                   -6      -5      -4      -3      -2          -1


# # using positive index
# print(tuple_items[3])
# # acess using negative index
# print(tuple_items[-1])
# # access using negative index
# print(tuple_items[-6])
# # access using range
# print(tuple_items[0:3])

# # start to second index
# print(tuple_items[:3])
# # second index to last
# print(tuple_items[3:])

# # to iterate all values in tuple
# for x in tuple_items:
#     print(x)

# # # tuple allow duplicate
# tuple_items1 = [10,20,30,40,50,60,10,20]
# print(tuple_items1)


# tuple length
# tuple_items1 = [10,20,30,40,50,60,10,20]
# print(len(tuple_items1))

# # tuple with single item
# tuple2 = (2)            #it is not tuple it is int type object
# print(tuple2)
# print(type(tuple2))

# tuple3 = (2,)                #it is  tuple class object
# print(tuple3)
# print(type(tuple3))


# # packing and unpacking in tuple
# fruit = ["apple","banana","mango","pineapple"]
# (red,*yellow,green) = fruit
# print(red)
# print(yellow)
# print(green)

# # join tuple
# tuple1 = [1,2,3,4,5]
# tuple2 = [6,7,8,9,10]
# # add tuple
# tuple3=tuple1+tuple2
# print(tuple3)
# # multiply tuple
# tuple4 = tuple1*2
# print(tuple4)



# function working on tuple

# count
# tuple6 = [1,1,2,3,4,1,3,2,6,5,2,1,1]
# # print(tuple6.count(1))
# var_set = set(tuple6)
# print(var_set)
# for x in var_set:
#     print(x,":",tuple6.count(x))

