"""
Given n non-negative integers representing an elevation
map where the width of each bar is 1, compute how much
water it can trap after raining
"""

height = [0,1,0,2,1,0,1,3,2,1,2,1]
#height = [2,1,0,1,3]
#height = [6,0,4]
#height = [5,4,1,3,4]
# brute force
# the first and last element cannot hold water, it will spill
for i in range (1,len(height)-1):
    #find right highest and left highest and find their minimum
    #find left highest
    j = i
    #left_high = 0
    left_high = 0
    right_high =0
    while j > 0 :
        if(height[j-1] > height[j]) :
            left_high = height[j-1]
        j -= 1
        #print(left_high)

    k = i
    while k < len(height)-1:
        if (height[k+1] > height[k]) :
            right_high = height[k+1]
        k += 1
        #print(right_high)

    waterAtPos = min(left_high,right_high) - height[i]
    if(waterAtPos > 0):
        print(waterAtPos)
# not working for input in line 7 , rest of the cases are working

