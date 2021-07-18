# Fizz Buzz
# For a given range example 1 to 50
# For multiples of 3 insert Fizz in the list
# For multiples of 5 insert Buzz in the list
# For multiples of 3 & 5 insert FizzBuzz
# return the list
#
# Learnings: Mutliples of 3 and 5 can be found by doing % 15 and would save one if condition

#Function to validate input type and to check if input greater than one.
def processInput(input):
    inputType = type(input)
    print(inputType)
    if(str(inputType) == "<class 'int'>"):
        print("valid input")
    else:
        print("invalid input")
        #raise Exception("Sorry, invalid input")
        exit()
    if(input < 1):
        print("Invalid input", + input)
        exit()


def fizzBuzz(iprange):
    processInput(iprange)
    myList = []
    for input in range(1,iprange):
        if(input%15 == 0):
            print("FizzBuzz", end =" ")
            myList.append("FizzBuzz")
            continue
        elif(input%5 == 0):
            print("Buzz", end =" ")
            myList.append("Buzz")
            continue
        elif(input%3 == 0):
            print("Fizz", end =" ")
            myList.append("Fizz")
            continue
        else:
            print(input, end =" ")
            myList.append(input)
    return myList

#Vary the inputs(normal scenarios and boundary scenarios) example: -1 , 0 , "hello" , 1.49 etc
result = fizzBuzz(25)
print(len(result))
for x in range(len(result)):
    print(x, end =" ")
    print(result[x], end =" ")

