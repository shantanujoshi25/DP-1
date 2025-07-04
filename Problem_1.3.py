# // Time Complexity : O(amount*coins) 
# // Space Complexity : O(amount)
#dynamic programming

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [float("inf") for i in range(amount+1)]
        dp[0] = 0

        
        for i in coins :
            for j in range(1,amount+1):

                if(j >= i):
                    dp[j] = min(dp[j-i]+1,dp[j])
                    
        if(dp[amount] == float("inf")):
            return -1
        return dp[amount]