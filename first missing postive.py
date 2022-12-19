class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
	    
        i=0
        while i<len(nums):
            crt=nums[i]-1
			# sorting array by ignoring negative numbers and higher numbers than len(nums)
            if  nums[i]>=0 and nums[i]<len(nums) and nums[i]!=nums[crt]:
                nums[i],nums[crt]=nums[crt],nums[i]
            else:
                i+=1 
        print(nums)
		# case1:    index != value-1  ==> requried answer
		#case2:    all elements are continuous index==value-1 ==> len(nums)+1 
        for i in range(len(nums)):
            if nums[i]-1!=i:
                return i+1 
        return len(nums)+1
