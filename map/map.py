'''
    This function take one argument and triple that argument print it and double that argument and 
    return
'''

def fun(x):
    print(x*3)
    return x*2

'''
    map function call one fun function by taking argument from list 
'''
x = map(fun,(10,20,30,40,50))

'''
print final list 
'''
print(list(x))