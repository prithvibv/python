"""
Triplets
Given an array containing N integers, and an number S
denoting a target sum.
Find all distinct integers that can add up to form target
sum. The numbers in each triplet should be ordered in
ascending order, and triplets should be ordered too.
Return empty array if no such triplet exists.
"""
"""
Machine generated alternative text:
Input
array = [1 2, 3, 4, 5, 6, 7, 8, 9, 15]
target = 18
Output
[[1,2,15],
[3,7,8],
[4,6,8],
[5,6,7]
]
"""
#Brute force
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 15]
sum = 18

for i in range(len(array)):
    for j in range(len(array)):
        for k in range(len(array)):
            if(i==j and j==k):
                continue
            if((array[i]+array[j]+array[k]) == sum ):
                result = (array[i],array[j],array[k])
                print(result)
print("O(n^3) approach")

#Optimized approach
array.sort()
print(array)

# learning of sorting
"""
array.sort(reverse=True)
print(array)

# take second element for sort
def takeSecond(elem):
    return elem[1]

# random list
random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# sort list with key
random.sort(key=takeSecond)

# print list
print('Sorted list:', random)
"""