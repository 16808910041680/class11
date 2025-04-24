a = int (input("How many rows do you want for the diamond? "))
b = a // 2
if b == 0:
    a / 2 
elif b == 1: 
    a = (a + 1) / 2

for i in range (1, b + 1):
    for j in range (1, i + 1):
        print ("*", end = "")
    print ("")