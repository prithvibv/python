'''
Base 5 number system decimal=[0,1,2,3,4,5,6,7,8,9] base5=[0,1,2,3,4,10,11,12,13,14]
Base 5 allowed digits is 0,1,2,3,4
'''
""" 
inputRange = 15

for i in range(inputRange):
    print(i) """
#419/5 = 83 , r = 4
#83/5 = 16  , r = 3
#16/5 = 3   , r = 1
#answer 3134

#print(419//5)
#print(419%5)
#inputNumber = 419
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
    #print(result)
    result.reverse()
    return listToInt(result)

ip = 10

for i in range(ip):
    #print(ipi)
    print(base5Number(i))

