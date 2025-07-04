# // Time Complexity : O(2^amount) 
# // Space Complexity : O(amount)


#recursion - pick not pick
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        minCoins = 0
        index = 0
        minCoins = self.recur(coins, index, amount, minCoins)
        if(minCoins == float("inf")):
            return (-1)
        return minCoins

    def recur(self, coins, index, TargetAmount, minCoins):
        
        # base case
        if(index<0 or index==len(coins)):
            return float("inf")
        elif( TargetAmount == 0 ):
            return minCoins
        # case 1 = dont pick the current index
        case1 = self.recur(coins, index + 1, TargetAmount, minCoins)

        # case 2 = pick the current index
        if(coins[index] <= TargetAmount):
            case2 = self.recur(coins, index, TargetAmount-coins[index], minCoins+1)        
        else:
            case2 = float("inf")

        return min(case1,case2)
