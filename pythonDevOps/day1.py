#day1
#task1
# Task 1: Learn how you can create a string, an integer and an array.
#Write a program to initialize string, int variable and use them.

stri = "Hello python devops"
print(stri)

intVar = 10
print(intVar)

list = [1,2,3,4,5]

for i in list:
    print(i)

for i in range(len(list)):
    print(i)

for i in range(0,100):
    if(i%2==0):
        print("Even number"+str(i))

for i in range(0,100):
    if(i%2!=0):
        print("Odd number"+str(i))