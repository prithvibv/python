# Fizz Buzz

# improved varaint 5 , improvement its introducing complexity, for input of size 100.
#Normal code 300 operations
# v3 code 100+33*2(66)+20*2(40)+6 = 212 operations,close to 30 % improvement.

#Learnings: List starts at 0, remove element at index use del list[index], normal insert(index,value), it will not replace it will move the list to the left example ['Fizz', 1, 2, 3, 4, 5, 6, 7, 8, 9] insert at zeroth position.

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

def fizzBuzzv5(inputRange):
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
fizzBuzzv5(50)
