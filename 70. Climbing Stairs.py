# [3/11/2024]5m out of 20m
""" 
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45
 """

class Solution:
    # Memoization
    def climbStairs(self, n: int) -> int:
        memo = {}
        return self.__climbStairs(n, memo)
    
    def __climbStairs(self, n: int, memo: dict[int, int]):
        if n in memo:
            return memo[n]
        elif n == 1:
            memo[1] = 1
        elif n == 2:
            memo[2] = 2
        else:
            memo[n] = self.__climbStairs(n-1, memo) + self.__climbStairs(n-2, memo)
        return memo[n]
