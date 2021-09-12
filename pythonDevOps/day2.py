#task1
#Task 1: WAP to create a function which returns the sum of all the element provided to it as an arguement. The arguement list will be dynamic.

def variableArgs(*args):
    for arg in args:
        print(arg)

variableArgs('Hello', 'Welcome', 'to', 'GeeksforGeeks')

def variableArgsSum(*args):
    sum = 0
    for arg in args:
        sum += arg
    print("sum: " + str(sum))

variableArgsSum(10,20,30,50)


def addition(*args):
   result = 0
   for i in args:
      result += i
   return result

print(addition(10,20,30,50))

def kwArgs(**kwargs):
    for key, value in kwargs.items():
        print ("%s == %s" %(key, value))

kwArgs(a=1,b=2,c=3)