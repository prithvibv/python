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
"""
Maintain a list on how to solve the problem with 2 lines description
"""
"""
1,2,3,4,5(i),6,7(k)
n-2 because we have loop till last but one element, as last element is held by k
prateek is using <=n-3
important problem asked in most companies.
n-3 more understading is required
we need to have atleast 4 elements to start with , other wise it will only 3 elements and we could easily compute the result.No need for algorithm.
"""
array = [13, 1, 43, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15]
sum = 18

array.sort()
# (length - 3) because we need at min of 4 elements else we will have 3 elements and can directly compute the sum.
# The for loop range it prints till the limit specified
#1(i),2(j),3,4(k)
rangeLimit = len(array) - 3
""" print(array)
print("length"+str(len(array)))
for k in range(rangeLimit):
    print(array[k]) """
for k in range(rangeLimit):
    i=k+1
    j=len(array)-1

    while(i<j):
        current_sum = array[k]
        current_sum += array[i]
        current_sum += array[j]
        if(current_sum == sum):
            print((array[k],array[i],array[j]))
            i = i + 1
            j = j - 1
        if(current_sum < sum):
            i = i + 1
        if(current_sum > sum):
            j = j - 1
