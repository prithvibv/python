# Fizz Buzz improved variant 4
# Improved variant 4
# think in terms of input range, like 1 to 100 , 33 mutliples of 3 and 20 multiples of 5 and 6 multiples of 15 so find solution such that if condition with multiples of 15 gets executed least amount of times.
# the if(mod3 and mod5) is placed in the second if(i % 5 == 0), it would save 50 if confdition statements

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

def fizzBuzzv4(inputRange):
    processInput(inputRange)
    resultList = []
    for i in range(1,inputRange):
        result = ""
        mod3 = False
        mod5 = False
        if(i % 3 == 0):
            result = "Fizz"
            mod3 = True
        if(i % 5 == 0):
            result = "Buzz"
            mod5 = True
            # mod 3 if condition saves n if conditions
            if(mod3):
                result = "Fizz Buzz"
        if(result == ""):
            result = i
        resultList.append(result)
    return resultList

result = fizzBuzzv4(50)
print(result)
