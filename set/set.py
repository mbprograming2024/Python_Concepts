# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members
# syntax to write set variable
var_set = {10,20,30,40,50}    # Sysntax {}

# # order of printing is not same
# print(var_set)

# # not a interable
# You cannot access items in a set by referring to an index or a key.
# print(var_set[0])               #error

# # length of set variable
# print(len(var_set))

# # you can perform loop operation through set but secuance of printing not confirm
# for x in var_set:
#     print(x)

# # change item
# var_set[1] = 30             #'set' object does not support item assignment
# print(var_set)

# # add item
# # Once a set is created, you cannot change its items, but you can add new items.
# var_set.add(60)
# print(var_set)


# # # remove
# # if value exist remove function remove the value otherwise though an error
# var_set.remove(50)
# print(var_set)

# discard
# if value exist discard function remove the value otherwise no any effect show
# var_set.discard(100)
# print(var_set)

# # pop()
# # it remove variable from last but set is not a order
# print(var_set.pop())
# print(var_set)

# # clear
# # clear empties the clear
# print(var_set.clear())
# print(var_set)

# # del
# # del kayword delete the set_var completely
# del var_set
# print(var_set)

# # union
# set1 = {1,2,3}
# set2 = {4,5,6}
# set1.union(set2)
# print(set1)


# set1 = {1,2,3}
# set2 = {4,5,6}
