# [3/25/2024]Time up
# Editorial
# 42%/7%
""" 
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
 """
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.n=n
        self.ans=[]
        self.backtrack([],0,0)
        return self.ans
        
    def backtrack(self, curr:List[str], openCount:int, closeCount:int):
        if openCount+closeCount==2*self.n:
            self.ans.append("".join(curr))
            return
        if openCount!=self.n:
            curr.append("(")
            self.backtrack(curr,openCount+1,closeCount)
            curr.pop()
        if closeCount<openCount:
            curr.append(")")
            self.backtrack(curr,openCount,closeCount+1)
            curr.pop()
