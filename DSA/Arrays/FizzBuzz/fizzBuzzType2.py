""" Replace number containing digit 3 or 5: Instead of replacing numbers that have 3 or 5 as a factor, the game can be played by replacing numbers containing the digit 3 or 5 with “fizz” or “buzz”.
For Example: 1, 2, Fizz, 4, Buzz, 6, 7, 8, 9, 10, 11, 12, Fizz, 14, Buzz, 16, 17, 18, 19, 20, 21, 22, Fizz, 24, Buzz, 26, 27, 28, 29, Fizz, Fizz, Fizz, Fizz, Fizz, Fizz Buzz, Fizz, Fizz, Fizz, Fizz, 40, 41, 42, Fizz, 44, Buzz, … """
'''
Learnings:
In Python, there are two types of division operators:
/ : Divides the number on its left by the number on its right and returns a floating point value.
// : Divides the number on its left by the number on its right, rounds down the answer, and returns a whole number.
problem:
Replace number containing digit 3 or 5
'''

def getDigit(input):
    digitList = []
    while(input > 0):
        #print(input%10)
        digitList.append(input%10)
        input = input // 10
    return digitList

#Recursion needs to have an if else condition , in if how to come out of infinite loop and else call itself
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