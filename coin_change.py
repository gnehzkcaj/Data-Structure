# refer to quick_sort.py
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        n = len(coins)
        MAX = amount + 1
        # 初始化 dp 表
        dp = [[0] * MAX for _ in range(n + 1)]
        # 状态转移：首行首列
        for a in range(1, MAX):
            dp[0][a] = MAX
        # 状态转移：其余行列
        for i in range(1, n + 1):
            for a in range(1, MAX):
                if coins[i - 1] > a:
                    # 若超过目标金额，则不选硬币 i
                    dp[i][a] = dp[i - 1][a]
                else:
                    # 不选和选硬币 i 这两种方案的较小值
                    dp[i][a] = min(dp[i - 1][a], dp[i][a - coins[i - 1]] + 1)
        return dp[n][amount] if dp[n][amount] != MAX else -1
        
coins = [1, 2,5]
amount = 11
print(Solution().coinChange(coins, amount))

coins = [2]
amount = 3
print(Solution().coinChange(coins, amount))


import math
print(2**6)
print(6*math.log(6, 2))