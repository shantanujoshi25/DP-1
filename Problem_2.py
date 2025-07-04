# // Time Complexity : O(nums) 
# // Space Complexity : O(1)
# Using Dynamic Programming

class Solution:
    def rob(self, nums: List[int]) -> int:

        if(len(nums)<3):
            return max(nums)
        #dp = [float("inf") for i in range(len(nums)+1)]
        #dp[0],dp[1],dp[2] = 0,nums[0],nums[1]
        

        # for i in range(3,len(nums)+1):
        #     dp[i] = nums[i-1] + max(dp[i-2],dp[i-3])

        # return max(dp[-1],dp[-2])
        
        nums[2] = nums[2] + nums[0]
        for i in range(3,len(nums)):
            nums[i] = nums[i] + max(nums[i-2],nums[i-3])
        return max(nums[-1],nums[-2])

        