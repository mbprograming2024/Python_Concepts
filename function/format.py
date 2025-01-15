name = "John"
age = 30

result = "My name is " + name + " and I am " + str(age) + " years old."
print(result)

# -----------------------------------------------------------------------


name = "John"
age = 30

result = "My name is %s and I am %d years old." % (name, age)
print(result)

# -----------------------------------------------------------------------


name = "John"
age = 30

result = "My name is {} and I am {} years old.".format(name, age)
print(result)

#-----------------------------------------------------------------------

name = "John"
age = 30

result = f"My name is {name} and I am {age} years old."
print(result)
