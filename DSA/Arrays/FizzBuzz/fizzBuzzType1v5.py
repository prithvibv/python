# Fizz Buzz

# improved varaint 5 , improvement its introducing complexity, for input of size 100.
#Normal code 300 operations
# v3 code 100+33*2(66)+20*2(40)+6 = 212 operations,close to 30 % improvement.

#Learnings: List starts at 0, remove element at index use del list[index], normal insert(index,value), it will not replace it will move the list to the left example ['Fizz', 1, 2, 3, 4, 5, 6, 7, 8, 9] insert at zeroth position.

# delete operation: delete the element and move the entire list left , this may be causing performance delay
#50 lakh inputs time taken 75seconds
# for 50 lakh inputs delete is taking extra 10 seconds
# removing one for loop took 53 seconds
#removing second for loop took 36 seconds

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
    #print(resultList)

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

    #print(resultList)
fizzBuzzv5(50)
#Profiling with 1 lakh input, extrapolation for 1 crore inputs would be 182 seconds 
""" import cProfile
cProfile.run('fizzBuzzv5(500000)') """

"""
         160002 function calls in 1.822 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    1.822    1.822 <string>:1(<module>)
        1    0.626    0.626    1.820    1.820 fizzBuzzType1v5.py:22(fizzBuzzv5)
        1    0.000    0.000    1.822    1.822 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
   159998    1.194    0.000    1.194    0.000 {method 'insert' of 'list' objects}
"""

