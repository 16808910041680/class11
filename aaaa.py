a = int (input("Enter a number: "))
c = a + 1
b = "*"
for i in range (1, c):
    if i == a:
        print (b * i)
        print ("command stopped")
    elif i == 1:
        print ("command started")
        print (b * i)
        i = i + 1
    else:
        print (b * i)
        i = i + 1
