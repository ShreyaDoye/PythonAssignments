"""for i in range(0,5):        ###i ki valu 4 tak jayegi  means 4 row
    for j in range(i):      ###j ki value 3 tak jayegi means 4 colume 0123
        print("*",end=' ')
    print()

i=int(input("Enter value of i:"))
for a in range(0,i+1):
    for j in range(a):
        print("*",end=' ')
    print()   """

for i in range (5,0,-1):
    for j in range(i):
        print("*",end=' ')
    print()