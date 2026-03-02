class Solution(object):
    def coinChange(self, coins, amount):
        dp = [amount + 1] * (amount + 1)
        
        dp[0] = 0
        
        for curr_amount in range(1, amount + 1):
            for coin in coins:
                if coin <= curr_amount:
                    dp[curr_amount] = min(dp[curr_amount], dp[curr_amount - coin] + 1)

        if dp[amount] > amount:
            return -1
        else:
            return dp[amount]