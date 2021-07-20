""" Change of Base:The game can be played in a mathematical base other than 10. For example, playing in base 5 would proceed as follows:
For Example: 1, 2, Fizz, 4, Buzz, Fizz, 12, 13, Fizz, Buzz, 21, Fizz, 23, 24, Fizz Buzz, 31, 32, Fizz, 34, Buzz, Fizz, … """

'''
Base 5 number system decimal=[0,1,2,3,4,5,6,7,8,9] base5=[0,1,2,3,4,10,11,12,13,14]
Base 5 allowed digits is 0,1,2,3,4
'''
#Base 5 manual caculation
#419/5 = 83 , r = 4
#83/5 = 16  , r = 3
#16/5 = 3   , r = 1
#answer 3134

#combining digits in the list
def listToInt(ip):
    r = ""
    for i in ip:
        r += str(i)
    return int(r)

def base5Number(inputNumber):
    result = []
    while inputNumber > 4:
        r = inputNumber % 5
        result.append(r)
        inputNumber = inputNumber // 5
    result.append(inputNumber)
    result.reverse()
    return listToInt(result)

#ip = 10

""" for i in range(ip):
    #print(ipi)
    print(base5Number(i)) """

def fizzBuzz(inputRange):
    resultList = []
    for n in range(1,inputRange):
        i = base5Number(n)
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

print(fizzBuzz(3))