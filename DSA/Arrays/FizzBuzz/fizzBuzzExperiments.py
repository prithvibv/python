# Fizz Buzz
# For a given range example 1 to 50
# For multiples of 3 insert Fizz
# For multiples of 5 insert Buzz
# For multiples of 3 & 5 insert FizzBuzz
# return the list
# important point to remember mutliples of 3 and 5 can be found by doing % 15 and would save one if condition

#Function to process input which validates the given input is greater than 1 and its an integer
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
            myList.append("Fizz")
    return myList

#Vary the inputs -1 , 0 ,
""" result = fizzBuzz(25)
print(len(result))
for x in range(len(result)):
    print(x, end =" ")
    print(result[x], end =" ") """

# Improved variant

def fizzBuzzv1(inputRange):
    processInput(inputRange)
    resultList = []
    for i in range(1,inputRange):
        result = ""
        if(i % 3 == 0):
            result = "Fizz"
        if(i % 5 == 0):
            result = "Buzz"
            if(i % 3 == 0 and i % 5 == 0):
                result = "Fizz Buzz"
        if(result == ""):
            result = i
        resultList.append(result)
    return resultList

""" result = fizzBuzzv1("Hello")
print(result) """

# boundary input 1 is giving weird result
# possible inputs
# empty
# zero
#-1
#1
#last number in integer, no max value, depends on size of the memory
#String value

# Improved variant2
# think in terms of input range, like 1 to 100 , 33 mutliples of 3 and 20 multiples of 5 and 6 multiples of 15 so find solution such that if condition with multiples of 15 gets executed least amount of times.
# the if(mod3 and mod5) is placed in the second if(i % 5 == 0), it would save 50 if confdition statements

def fizzBuzzv2(inputRange):
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
            # mod 3 and mod5 inside i%5 if condition saves n if conditions
            if(mod3 and mod5):
                result = "Fizz Buzz"
        if(result == ""):
            result = i
        resultList.append(result)
    return resultList

""" result = fizzBuzzv2(50)
print(result)
 """
#calculating elapsed time
""" import time

start = time.time()
print("hello")
end = time.time()
print(end - start) """
# improved varaint 3 , improvement its introducing complexity, for input of size 100.
#Normal code 300 operations
# v3 code 100+33*2(66)+20*2(40)+6 = 212 operations,close to 30 % improvement
def fizzBuzzv3(inputRange):
    #startIndex = 1
    resultList = []

    for i in range(inputRange):
        #print(i,end=" ")
        resultList.insert(i,i)
    print(resultList)

    for i in range(0,inputRange,3):
        if(i == 0):
            continue
        #print(i,end=" ")
        del resultList[i]
        resultList.insert(i,"Fizz")

    for i in range(0,inputRange,5):
        if(i == 0):
            continue
        #print(i,end=" ")
        del resultList[i]
        resultList.insert(i,"Buzz")

    for i in range(0,inputRange,15):
        if(i == 0):
            continue
        #print(i,end=" ")
        del resultList[i]
        resultList.insert(i,"Fizz Buzz")

    print(resultList)
fizzBuzzv3(50)

""" resultList = []
startIndex = 1
inputRange = 10
for i in range(startIndex,inputRange):
        resultList.insert(i,i)
print(resultList)
del resultList[0]
resultList.insert(0,"Fizz")
print(resultList) """

#today's learnings , list starts at 0, remove element at index use del list[index], nomral insert(index,value), it will not replace it will move the list to the left example ['Fizz', 1, 2, 3, 4, 5, 6, 7, 8, 9] insert at zero position


{"mode":"full","isActive":false}