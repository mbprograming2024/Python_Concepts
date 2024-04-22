import json

# a = [1,2,3,4,5,6]
# print(json.dumps(a))
# print(type(json.dumps(a)))
   
b = {"name":"mayur"}
print(b)
print(type(b))
c = json.dumps(b)
print(type(c))
print(c)
print(json.loads(c))
print(type(json.loads(c)))