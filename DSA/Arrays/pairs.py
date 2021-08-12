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
        result = (x,array[i])
        print(result)

    tempSet.add(array[i])
"""
Set learnings:
initialize empty set like tempSet = set()
initialize set with elements
tempSet = {1,2,3}

#tuple learnings:
tuple_ex = ("apple","banana","grapes")
"""

"""
two pair will work if the array is sorted , i was trying with an unsorted array so things did not work out
"""
# two pointer solution
# 1 must be a sorted array
# 2 keep first pointer i at first element and j at last element, if sum of two elements less than target sum increment i pointer (starting pointer) and sum of 2 elements greater than target sum decrement the j the last pointer.
#sort function will sort the array no need to take store the result original array gets sorted
print("two pointer")
array = [13, 1, 43, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15]
sum = 18

array.sort()
print(array)
i=0
j=len(array)-1

while(i<j):
    if(array[i]+array[j] == sum):
        print((array[i],array[j]))
        i = i + 1
        j = j - 1
    if(array[i]+array[j] < sum):
        i = i + 1
    if(array[i]+array[j] > sum):
        j = j - 1








