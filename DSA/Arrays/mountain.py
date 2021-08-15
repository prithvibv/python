"""
Mountain
Write a function that takes input an array of distinct
integers, and returns the length of highest mountain.
A mountain is defined as adjacent integers that are
strictly increasing until they reach a peak, at which the
become strictly decreasing.
At least 3 numbers are required to form a mountain.
"""





""" input = [5,6,1,2,3,4,5,4,3,2,0,1,2,3,-2,4]
#expected output is 9
result = []
limit = len(input)-1
for i in range(1,limit):

    if((input[i] > input[i+1]) and (input[i] > input[i-1]) ):
        print("peak found"+str(input[i]))

        j = i - 1
        #j -= 1
        count = 1
        while( input[j] > input[j-1] and j >= 1 ):
            j -= 1
            count += 1
        print("left slope"+str(count))
        k= i + 1
        #k += 1
        rightSlope = 1
        while(input[k] > input[k+1] and k < limit-1):
            k += 1
            #count += 1
            rightSlope += 1
        count = count + rightSlope
        result.append(count)
        print("rightslope"+str(rightSlope))
        print("total length"+str(count))


print(max(result))
 """

def mountain(input):
    result = []
    print("Mountain function")
    print(input)

    for i in range(1,len(input)-1):

        if(input[i] > input[i-1] and input[i] > input[i+1]):
            print("peak"+str(input[i]))
            # left slope
            j = i
            count = 0
            leftSlope = 0
            while(j > 1 and input[j] > input [j-1]):
                leftSlope += 1
                count += 1
                j -= 1
            print("Left slope "+str(leftSlope))

            # right slope
            k = i
            rightSlope = 0
            while(k < len(input)-1 and input[k] > input [k+1]):
                rightSlope += 1
                count += 1
                k += 1
            print("Right slope "+str(rightSlope))
            print(count)
            result.append(count)
    return max(result)

input = [5,6,1,2,3,4,5,4,3,2,0,1,2,3,-2,4]
r = mountain(input)
print("result:"+str(r))