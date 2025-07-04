# // Time Complexity : O(2^amount) 
# // Space Complexity : O(amount)
#recursion - pick not pick
#memoization
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}
        minCoins = 0
        index = 0
        minCoins = self.recur(coins, index, amount, minCoins,memo)
        if(minCoins == float("inf")):
            return (-1)
        return minCoins

    def recur(self, coins, index, TargetAmount, minCoins, memo):
        # base case
        if((TargetAmount,index) in memo):
            minC = memo[(TargetAmount,index)] + minCoins
        else:
            if(index<0 or index==len(coins)):
                return float("inf")
            elif( TargetAmount == 0 ):
                return minCoins
            # case 1 = dont pick the current index
            case1 = self.recur(coins, index + 1, TargetAmount, minCoins,memo)

            # case 2 = pick the current index
            if(coins[index] <= TargetAmount):
                case2 = self.recur(coins, index, TargetAmount-coins[index], minCoins+1,memo)        
            else:
                case2 = float("inf")

            minC =  min(case1,case2)

            memo[(TargetAmount,index)] = minC - minCoins

        return minC