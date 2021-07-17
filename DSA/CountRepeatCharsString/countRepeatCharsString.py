#Count repeated chars in a String
#learnings: initialize the list with zero and specify the size charCounter = [0] * 256
# ord() --> retruns unicode value used here to get ascii value
# chr() --> returns char for ascii value
# print does not concatenate string with int, we need to use to str() to convert to string

def countRepeatCharsString(inputString):
    charCounter = [0] * 256
    for i in range(len(inputString)):
        c = ord(inputString[i])
        charCounter[c] += 1

    for i in range(len(charCounter)):
      if(charCounter[i] > 1):
        print("repeated character:"+chr(i))
        print("repeat count:"+str(charCounter[i]))


input = ['n','a','v','a','n','e','e','t','h','a']
papa = ['p','r','i','t','h','v','i']
countRepeatCharsString(input)