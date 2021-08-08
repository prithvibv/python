#first solve the problem brute force
#do improvemnets on top of it
# see life at google coding interview sample problems

"""
Pairs
Given an array containing N integers, and an number S
denoting a target sum.
Find two distinct integers that can pair up to form target
sum. Let us assume there will be only one such pair.
Input
array = [10, 5, 2, 3, -6, 9, 11 ]
"""
array = [10, 5, 2, 3, -6, 9, 11 ]
s = 4
print("input: "+ str(array))
#Brute force : O(n^2)
for i in range(len(array)):
    for j in range(len(array)):
        if(array[i] == array[j]):
            continue
        if(array[i]+array[j] == s):
            print("pair found"+ str(array[i]) +""+ str(array[j]))

# optimised
"""
sort 
-6,2,3,5,9,10,11
-6 + ( ) = 4
10
Just look for 10 in (2,3,5,9,10,11) may using binary search
O(n(logn))
"""
"""
more optimized
use a unordered set
take the first element from the array say 10 and see if 10-x =4, x = -6 is in the array, if its there return else insert the element. see pairs prateek video for more information
O(N)
"""
print("O(n)")
array = [10, 5, 2, 3, -6, 9, 11 ]
s = 4
tempSet = set()

for i in range(len(array)):
    x = 4 - array[i]
    if(x in tempSet):
        print( "Pair found:" + str(x) +" "+str(array[i]))
    else:
        tempSet.add(array[i])
"""
Set learnings:
initialize empty set like tempSet = set()
initialize set with elements
tempSet = {1,2,3}
"""





