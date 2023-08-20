def fizzBuzz(number):
    result = []
    for element in range(1,number):
            if element%3 == 0 and element%5 == 0: #This can be element%15 == 0
                result.append("FizzBuzz")
            elif element%3 == 0:
                result.append("Fizz")
            elif element%5 == 0:
                 result.append("Buzz")
            else:
                 result.append(element)
    return result

funResult = fizzBuzz(31)
print(funResult)