# Fizz Buzz improved variant 1
#Concept: The below if condition
# if(i % 3 == 0 and i % 5 == 0):
#
# is nested inside the
#if(i % 5 == 0):
#The idea is obtained from input analysis
#Say input from 1 to 50 , in the previous program fizzBuzz, for all the inputs 1 to 50, all the three if conditions are run, in order to minimise the execution, %3 if condition is placed first, %5 condition is second, %3 and %5 is placed inside %5 which would save around 40 if condition checks.

#improvements: think of using insert instead of append it may save speed.

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

# Improved variant

def fizzBuzzv2(inputRange):
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

result = fizzBuzzv2(35)
print(result)


""" #Profiling info
import cProfile
cProfile.run('fizzBuzzv2(10000000)') """
"""
10000006 function calls in 4.131 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)     
        1    0.075    0.075    4.131    4.131 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 fizzBuzzType1v2.py:11(processInput)
        1    3.083    3.083    4.056    4.056 fizzBuzzType1v2.py:26(fizzBuzzv2)
        1    0.000    0.000    4.131    4.131 {built-in method builtins.exec}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.print}
  9999999    0.972    0.000    0.972    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
 """