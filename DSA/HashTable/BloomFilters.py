# Concept: we hash the input, by passing it to hash function 1 , 2 and 3 and results of the hash functions is marked as one in a bit array, while adding a word.
#While searching for a new word , again we pass the input to 3 different hash functions and check if all the bits are set. if all are set the word is available else not available, it can have false positives
#Applications: to check if username is available, quick searching
#murmur hash is designed for bloom filters. Its a fast hash function
#https://pypi.org/project/mmh3/
# now for different hash functions I am planning to use murmur with different seed values.
#https://www.geeksforgeeks.org/bloom-filters-introduction-and-python-implementation/
# pip install mmh3
#larger the bit array less false positives
#vary the bit array length at 150 size no false positives
import mmh3
""" print(mmh3.hash("foo")%10)
print(mmh3.hash("foo",3)%10)
print(mmh3.hash("foo",5)%10)
print(mmh3.hash("foo",7)%10) """
# Idea is to use different seed values 3,5,7

wordMap = [0] * (256)
sizeWordMap = 150
print(sizeWordMap)
#print(wordMap)

def add(input):
    hash1 = mmh3.hash(input,3)%sizeWordMap
    wordMap[hash1] = 1
    #print(hash1)
    hash2 = mmh3.hash(input,5)%sizeWordMap
    wordMap[hash2] = 1
    #print(hash2)
    hash3 = mmh3.hash(input,7)%sizeWordMap
    wordMap[hash3] = 1
    #print(hash3)

def search(input):
    matchcount=0
    hash1 = mmh3.hash(input,3)%sizeWordMap

    if(wordMap[hash1] == 1):
        #print("Hash1 matched"+str(hash1))
        matchcount+=1

    hash2 = mmh3.hash(input,5)%sizeWordMap
    if(wordMap[hash2] == 1):
        #print("Hash2 matched"+str(hash2))
        matchcount+=1

    hash3 = mmh3.hash(input,7)%sizeWordMap
    if(wordMap[hash3] == 1):
        #print("Hash3 matched"+str(hash3))
        matchcount+=1

    if(matchcount == 3):
        #print("****Bloom filter match found "+input)
        return True
    else:
        #print("Bloom filter match not found "+input)
        #print("match count"+str(matchcount))
        return False

""" print(add("Prithvi",10))
print(search("ithvi",10))
print(search("uma",10)) """

#print(wordMap)

word_present = ['abound','abounds','abundance','abundant','accessable','bloom','blossom','bolster','bonny','bonus','bonuses','coherent','cohesive','colorful','comely','comfort',
'gems','generosity','generous','generously','genial']
#print(word_present[:10])

word_absent = ['bluff','cheater','hate','war','humanity',
'racism','hurt','nuke','gloomy','facebook',         'geeksforgeeks','twitter']

test_words = word_present[:10] + word_absent

print(test_words)

for word in word_present:
    add(word)

for word in test_words:
    if search(word):
        if word in word_absent:
            print("'{}' is a false positive!".format(word))
        else:
            print("'{}' is probably present!".format(word))
    else:
        print("'{}' is definitely not present!".format(word))
print("bit array")
#print(wordMap)