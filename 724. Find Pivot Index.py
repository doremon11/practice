'''
[1,7,3,6,5,6]
[1,2,3]
[2,1,-1]
[-1,-1,0,0,-1,-1]

3
-1
0
2
solved by using left_sum and right_sum 
'''
 def pivotIndex(nums):
        s=sum(nums)
        left_sum=0
        for i,j in enumerate(nums):
            right_sum=(s-nums[i]-left_sum)
            if left_sum==right_sum:
                return i 
            left_sum+=nums[i]
        return -1

