"""
示例 1：

输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
示例 2：

输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 没有交易完成, 所以最大利润为 0。
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        length = len(prices)
        for i in range(length-1):
            for j in range(i+1, length):
                if prices[j] - prices[i] > max:
                    max = prices[j] - prices[i]
        return max

    def maxProfit2(self, prices: List[int]) -> int:
        inf = int(1e9)
        minprice = inf
        maxprofit = 0
        for price in prices:
            maxprofit = max(maxprofit, price - minprice)
            minprice = min(minprice, price)
        return maxprofit


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfit2([7, 1, 5, 3, 6, 4]))
    print(solution.maxProfit([7, 6, 5, 4, 3, 2]))



