# [3/11/2024]8 mins
from typing import List

""" 
1 <= prices.length <= 105
0 <= prices[i] <= 10^4 
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = 10**4
        maxProfit = 0
        for i in range(len(prices)):
            curr = prices[i]
            if curr < min:
                min = curr
                continue
            profit = curr - min
            if maxProfit < profit:
                maxProfit = profit
                continue
        return maxProfit
