
# case 1
# loop break using break statement 
for a in range(1,6):
    if a == 6:
        print("a=",6)
else:
    print("without break statement")

# case 2 :

for a in range(1,6):
    if a == 3:
        print("a=",3)
        break
else:
    print("with break statement")

# example :

for item in [1, 2, 3, 4]:
    if item == 3:
        print("Found 3!")
        break
else:
    print("3 not found.")