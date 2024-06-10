"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a
different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any
profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before
you sell.

Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_at_day = 0
        sell_at_day = 1
        while buy_at_day < len(prices) - 1:
            # print("buy at: " + str(buy_at_day))
            # earliest to buy on the first day
            # latest to buy one day before the last day
            sell_at_day = buy_at_day + 1
            profit = 0
            while sell_at_day < len(prices):
                # earliest to sell is on the second day
                # latest to sell is the last day
                # print("sell at: " + str(sell_at_day))
                profit = prices[sell_at_day] - prices[buy_at_day]
                if profit > max_profit:
                    max_profit = profit
                sell_at_day += 1
            buy_at_day += 1
        return max_profit if max_profit > 0 else 0 
    
    

s = Solution()

prices = [7,1,5,3,6,4]
print(s.maxProfit(prices))

prices = [7,6,4,3,1]
print(s.maxProfit(prices))
