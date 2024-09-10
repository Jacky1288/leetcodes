"""
给你一个整数数组 prices ，其中 prices[i] 表示某支股票第 i 天的价格。

在每一天，你可以决定是否购买和/或出售股票。你在任何时候 最多 只能持有 一股 股票。你也可以先购买，然后在 同一天 出售。

返回 你能获得的 最大 利润 。



示例 1：

输入：prices = [7,1,5,3,6,4]
输出：7
解释：在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5 - 1 = 4。
随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6 - 3 = 3。
最大总利润为 4 + 3 = 7 。

"""
from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:

        # [7,1,5,3,6,4]
        # 使用动态规划算法解题
        n = len(prices)
        if n == 0:
            return 0
        dp = [[0] * 2 for _ in range(n)]
        # 初始化持有股票后的现金情况
        # dp[i][0] 表示第 i 天结束时，如果不持有股票，手中持有的现金数。
        # dp[i][1] 表示第 i 天结束时，如果持有股票，手中持有的现金数。
        dp[0][0], dp[0][1] = 0, -prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])

        return max(dp[n - 1][0], dp[n - 1][1])


if __name__ == '__main__':
    solution = Solution()
    a = [7, 1, 5, 3, 6, 4]
    b = [7, 6, 4, 3, 1]
    c = [1, 2, 3, 4, 5]
    # print(solution.maxProfit(a))
    # print(solution.maxProfit(b))
    print(solution.maxProfit(a))
    print(solution.maxProfit(b))
    print(solution.maxProfit(c))
