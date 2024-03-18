# [3/18/2024]17m out of 30m
# 48%/29%
""" 
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
 

Follow up: Could you use search pruning to make your solution faster with a larger board?
 """
from typing import List, Tuple


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board=board
        self.word=word
        self.l=len(word)
        self.m=len(board)
        self.n=len(board[0])
        for i in range(self.m):
            for j in range(self.n):
                if self.backtrack(0, i, j, set()):
                    return True
                
        return False
    
    def backtrack(self, start: int, i: int, j: int, trace: set[Tuple[int,int]]) -> bool:
        if start==self.l:
            return True
        if i<0 or i>self.m-1 or j<0 or j>self.n-1:
            return False
        if (i,j) in trace:
            return False
        if self.board[i][j] != self.word[start]:
            return False
        
        trace.add((i,j))
        if self.backtrack(start+1, i-1, j, trace) or self.backtrack(start+1, i+1, j, trace) or self.backtrack(start+1, i, j-1, trace) or self.backtrack(start+1, i, j+1, trace):
            return True
        trace.remove((i,j))
        return False
