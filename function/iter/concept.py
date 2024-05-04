# The iter() function returns an iterator object.
# iter(object): When only one argument is provided, iter() tries to create an iterator from the given object. 
# If the object is an iterable (such as a list, tuple, string, etc.), 
# it returns an iterator object that allows iteration over the elements of the iterable.Example:


# fullname='MAYUR PRALHAD BAVISKAR'

# a = iter(fullname)

# print(next(a))
# print(next(a))
# print(next(a))
# print(type(a))   #<class 'str_ascii_iterator'>



# #############################################################
# iter(callable, sentinel): 
# When two arguments are provided, the first argument is a callable 
# (a function) and the second argument is a sentinel value. This form of iter() 
# creates an iterator that repeatedly calls the callable until it returns the sentinel value.
# The callable is called with no arguments.
# If the callable returns the sentinel value, the iterator stops.
# If the callable never returns the sentinel value, the iterator will continue indefinitely.


# import random

# def generate_random():
#     return random.randint(1, 10)

# random_iterator = iter(generate_random, 3)  # Calls generate_random until it returns 5

# print(list(random_iterator))


