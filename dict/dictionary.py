# # syntax
# # Dictionaries are used to store data values in key:value pairs.
# var_dict = {"name":"mayur","city":"nashik","age":25}
# print(var_dict)
#
# # how to access the dictionary items
# print(var_dict["name"])

# # for access kay
# for x in var_dict.keys():
#     print(x)
#
# #for access values
# for x in var_dict.values():
#     print(x)
#
# # for access the key and value both
# for x in var_dict.items():
#     print(x)

# # does not allow duplicat
# # does not allow duplicate it print last upadate value in bellow example name = maya print
# var_dict1 = {"name":"mayur","city":"nashik","age":25,"name":"maya"}
# print(var_dict1)

# # update or change the value
# var_dict1 = {"name":"mayur","city":"nashik","age":25}
# print(var_dict1)
# var_dict1["age"] = 26
# print(var_dict1)

# # add item
# # Update function change value if value exist in dictionary and add if does not exist in dictionary
# var_dict2 = {"name":"mayur","city":"nashik","mobile":7020611623}
# print(var_dict2)
# var_dict2.update({"age":26})
# print(var_dict2)

# # remove the item
# # pop() - remove the specified key with its corresponding value
# var_dict2 = {"name":"mayur","city":"nashik","mobile":7020611623}
# print(var_dict2.pop("name"))

# copy the dictionary
# var_dict5={"name":"mayur","city":"nashik","mobile":7020611623}
# var_dict4 = var_dict5
# print(var_dict4)
# var_dict4 = var_dict5.copy()
# print(var_dict4)

# nested dictionary
# dictionary inside another dictionary

# Create three dictionaries, then create one dictionary that will contain the other three dictionaries:

# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }
# child2 = {
#   "name" : "Tobias",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linus",
#   "year" : 2011
# }

# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3
# }
# print(myfamily)