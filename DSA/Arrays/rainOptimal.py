"""
Given n non-negative integers representing an elevation
map where the width of each bar is 1, compute how much
water it can trap after raining
"""

height = [0,1,0,2,1,0,1,3,2,1,2,1]
#height = [2,1,0,1,3]
#height = [6,0,4]
#height = [5,4,1,3,4]
# optimal solution
# the first and last element cannot hold water, it will spill

left_high = []
leftHigh = height[0]
right_high = []
rightHigh = 0

for i in range (len(height)):
    if(height[i] > leftHigh):
        leftHigh = height[i]
    left_high.insert(i,left_high)
print(left_high)
