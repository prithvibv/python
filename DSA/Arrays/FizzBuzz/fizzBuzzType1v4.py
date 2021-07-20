# Fizz Buzz improved variant 4
# Improved variant 4
# think in terms of input range, like 1 to 100 , 33 mutliples of 3 and 20 multiples of 5 and 6 multiples of 15 so find solution such that if condition with multiples of 15 gets executed least amount of times.
# the if(mod3 and mod5) is placed in the second if(i % 5 == 0), it would save 50 if confdition statements

#improvement: clear main memory for better performance

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
"""
#Profiling info
import cProfile
cProfile.run('fizzBuzzv4(10000000)')

 10000006 function calls in 4.393 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.077    0.077    4.393    4.393 <string>:1(<module>)
        1    3.269    3.269    4.315    4.315 fizzBuzzType1v4.py:20(fizzBuzzv4)
        1    0.000    0.000    0.001    0.001 fizzBuzzType1v4.py:7(processInput)
        1    0.000    0.000    4.393    4.393 {built-in method builtins.exec}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.print}
  9999999    1.046    0.000    1.046    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
 """

