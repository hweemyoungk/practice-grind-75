# [3/14/2024]Time up
# 96%/34%
""" 
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
 

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 2^31 - 1
0 <= amount <= 10^4
 """
from typing import List


class Solution:
    # BFS + memo
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if len(coins) == 0:
            return -1
        
        memo = set()
        targets = [amount - coin for coin in coins if amount >= coin]
        level = 1
        while targets:
            nextTargets = []
            for target in targets:
                if target == 0:
                    return level
                if target in memo:
                    continue
                # New target
                memo.add(target)
                nextTargets.extend([target - coin for coin in coins if target >= coin])
            targets = nextTargets
            level+=1
        return -1
    