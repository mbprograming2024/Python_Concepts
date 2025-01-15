# The try block lets you test a block of code for errors.
#
# The except block lets you handle the error.
#
# The else block lets you execute code when there is no error.
#
# The finally block lets you execute code, regardless of the result of the try- and except blocks.

# X=10
# try:
#     print(X)
# except :
#     print("an exception occured X is not define")
#

######################################################################
# The else block lets you execute code when there is no error.
#
# X=10
# try:
#     print(X)
# except :
#     print("an exception occured X is not define")
# else:
#     X=10+X
#     print("Nothing go wrong X=",X)

######################################################################

X=20
try:
    print(X)
except:
    print("X is Not define")
else:
    print("if X is define else will execute")
finally:
    print("indipendant on try it is execute ether X define or not define")