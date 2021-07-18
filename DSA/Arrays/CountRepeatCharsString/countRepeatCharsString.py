# Count repeated chars in an input array

# Concept: Keep an array of size 256 and initialize it to zero, when the string is parsed for every character that is read increment the count, for characters whose count greater than 1, the characters are repeated

#  Learnings: Initialize the list with zero and specify the size charCounter = [0] * 256
# ord() --> input: character, output: unicode value (ASCII value).
# chr() --> input: ASCII value, output: character
# Print does not concatenate string with int, we need to use to str() to convert to string

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
input2 = ['p','r','i','t','h','v','i']
countRepeatCharsString(input)