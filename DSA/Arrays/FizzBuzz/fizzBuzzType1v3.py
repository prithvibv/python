# Fizz Buzz improved variant 2
#Concept: The below if condition
# if(i % 3 == 0 and i % 5 == 0):
#
# is nested inside the
#if(i % 5 == 0):
# mod3 and mod 5 if condition is changed to only, mod3 as mod5 is already being checked in the previous step

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

def fizzBuzzv3(inputRange):
    processInput(inputRange)
    resultList = []
    for i in range(1,inputRange):
        result = ""
        if(i % 3 == 0):
            result = "Fizz"
        if(i % 5 == 0):
            result = "Buzz"
            if(i % 3 == 0):
                result = "Fizz Buzz"
        if(result == ""):
            result = i
        resultList.append(result)
    return resultList

result = fizzBuzzv3(35)
print(result)
