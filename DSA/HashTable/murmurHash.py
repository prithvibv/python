'''
https://www.youtube.com/watch?v=b8HzEZt0RCQ
VEry nice video
A good hash function should pass two tests
1. Chi square test
    A hash function should produce a uniform result(both at the center and the edges), but should be random (not like normal distribution where at the center uniform result and edge no results)
2. Avalanche test
    A single change in input bit should result in atleast 50% of bits changed in the result

Murmur: most beneficial, it passes both the tests
seed value : any randome number
'''

import mmh3

print(mmh3.hash("foo",3))
print(mmh3.hash("fob",3))
print(mmh3.hash("abc",3))
print(mmh3.hash("abd",3))


