
# count()	Returns the number of times a specified value occurs in a tuple
tuple.count(value)
# index()	Searches the tuple for a specified value and returns the position of where it was found

tup2 = (1,2,3,2,1,3,4,5,6)
print(tup2.count(2))
print(tup2.index(3))


# order,unchangeable,allow duplicate
# tuple1 = (1,2,3,2,1,3,4,5,6)
#print(tuple1)

# access tuple
#print(tuple1[2])


# for x in tuple1:
#     print(x)

# print(tuple1[2:])

# you can delete tuple 
# The del keyword can delete the tuple completely:
# del tuple1
# print(tuple1)



# Unpacking a Tuple

# tup = ("mayur","Pralhad","Baviskar")
# # print(tup)

# (son , father , lastname) = tup 

# print(son)
# print(father)
# print(lastname)

# tup = ("mayur","Pralhad","Baviskar","rushikesh","sital","asha")

# (son,father,lastname,*restfamily,mother) = tup

# print(restfamily)
