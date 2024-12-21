#Basic Star Pattern
print("Star Pattern \n")
for i in range(1,4):
    for j in range(i):
        print("H", end="")
    print('\n')

#Inverted Star Pattern
print("Inverted Star Pattern \n")
for i in range(4,1,-1):
    for j in range(i, 1,-1):
        print("H", end="")
    print('\n')
