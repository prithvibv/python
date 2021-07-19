# Count repeated chars in an input array

# Concept: Keep an array of size 256 (characters range) and initialize it to zero, when the string is parsed for every character that is read increment the count, for characters whose count greater than 1, the characters are repeated

#  Learnings: Initialize the list with zero and specify the size charCounter = [0] * 256
# ord() --> input: character, output: unicode value (ASCII value).
# chr() --> input: ASCII value, output: character
# print() does not concatenate string with int, we need to use to str() to convert the int to string
# len() --> length of the collection

#Improvement:
#1. to consider from small case a to capital case A, based on the input we have to decide the character set, then instead of 256 characters array we can keep limited character set.It would save memory.

def countRepeatCharsString(inputString):
    charCounter = [0] * 256
    for i in range(len(inputString)):
        #Find the ascii value of the character, increment the corresponding index by one.
        c = ord(inputString[i])
        charCounter[c] += 1

    for i in range(len(charCounter)):
      if(charCounter[i] > 1):
        print("repeated character:"+chr(i))
        print("repeat count:"+str(charCounter[i]))


input = ['n','a','v','a','n','e','e','t','h','a']
input2 = ['p','r','i','t','h','v','i']
countRepeatCharsString(input)