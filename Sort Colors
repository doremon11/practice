class Solution:
def sortColors(self, nums: List[int]) -> None:
"""
Do not return anything, modify nums in-place instead.
"""
high=len(nums)-1
low=0
mid=0
while mid<=high:
  if nums[mid]==0:
    nums[mid],nums[low]=nums[low],nums[mid]
    low+=1
    mid+=1
  elif nums[mid]==1:
    mid+=1
  else:
    nums[mid],nums[high]=nums[high],nums[mid]
    high-=1

**2nd way ** :

Count the number of 0’s, 1’s and 2’s. After Counting, put all 0’s first, then 1’s and lastly 2’s in the array.

class Solution:
def sortColors(self, nums: List[int]) -> None:
"""
Do not return anything, modify nums in-place instead.
"""
c0,c1,c2=0,0,0
for i in range(len(nums)):
  if nums[i]==0:
    c0+=1
  elif nums[i]==1:
    c1+=1
  else:
    c2+=1
for i in range(0,c0):
   nums[i]=0
for i in range(c0,c1+c0):
   nums[i]=1
for i in range(c1+c0,c2+c1+c0):
   nums[i]=2
