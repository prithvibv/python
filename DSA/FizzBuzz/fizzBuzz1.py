'''
In Python, there are two types of division operators:
/ : Divides the number on its left by the number on its right and returns a floating point value.
// : Divides the number on its left by the number on its right, rounds down the answer, and returns a whole number.
problem:
Replace number containing digit 3 or 5
'''

""" def getDigit(input):
    if(input < 10):
        if(input == 3):
            print("Fizz")
        elif(input == 5):
            print("Buzz")
        print(input)
    else:
        getDigit(input // 10)
        print(input % 10)
        #print(input)

getDigit(53) """


#from DSA.fizzBuzz import fizzBuzz


def getDigit(input):
    digitList = []
    while(input > 0):
        #print(input%10)
        digitList.append(input%10)
        input = input // 10
    return digitList
#resultList = getDigit(102)
#print(resultList)
#Recursion needs to have an if else condition , in if how to come out of inifinite loop and else call itself
""" def getDigitR(input):
    if(input < 10):
        print(input%10)
    else:
        getDigitR(input//10)
        print(input%10)

getDigitR(3432) """

def fizzBuzz(inputValue):
    resultList = []
    for i in range(0,inputValue):
        result = i
        digit3 = False
        digit5 = False
        print(i)
        digits = getDigit(i)
        if(3 in digits):
            result = "Fizz"
            digit3 = True

        if(5 in digits):
            result = "Buzz"
            digit5 = True

        if(digit3 and digit5):
            result = "Fizz Buzz"
            print(result)

        resultList.append(result)
    return resultList

print(fizzBuzz(36))