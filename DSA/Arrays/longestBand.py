"""
Longest Band
Given an array containing N integers, find length of
longest band.
A band is defined as a subsequence which can be re-
ordered in such a manner all elements appear
consecutive (ie with absolute difference of 1 between
neighbouring elements)
A longest band is the band (subsequence) which contains
maximum integers.
"""

input = [1,9,3,0,18,5,2,4,10,7,12,6,8]
#output = 8

""" def longestBand(input):
    result = []
    input.sort()
    count = 0
    for i in range(0,len(input)-1):
        if(input[i+1] - input[i] == 1):
            count+=1
        else:
            break
    result.append(count)
    print(result)

longestBand(input) """

def longestBand(input):
    mySet = set(input) # new learnings
    result = []
    print(type(mySet))
    for i in range (len(input)):
        # check if parent element is there else its the parent
        if(not( input[i] - 1 in mySet)):
            print("Parent element"+str(input[i]))
            parent = input[i]
            count = 0
            next_no = parent + 1
            while(next_no in mySet):
                next_no+=1
                count += 1
            print("parent"+str(parent)+"Count"+str(count))
            result.append(count)
    return max(result)

r = longestBand(input)
print(r)
