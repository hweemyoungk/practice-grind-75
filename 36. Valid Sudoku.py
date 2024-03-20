# [3/19/2024]17m out of 35m
# 48%/65%
""" 
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

Example 1:


Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
 """
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ord1=ord('1')
        visited=[False]*9
        for row in board:
            for n in row:
                if n=='.':
                    continue
                if visited[ord(n)-ord1]:
                    return False
                visited[ord(n)-ord1]=True
            visited=[False]*9
        for i in range(9):
            for row in board:
                n=row[i]
                if n=='.':
                    continue
                if visited[ord(n)-ord1]:
                    return False
                visited[ord(n)-ord1]=True
            visited=[False]*9
        for i in range(3):
            iStart=3*i
            for j in range(3):
                jStart=3*j
                for iCur in range(iStart, iStart+3):
                    for jCur in range(jStart, jStart+3):
                        n=board[iCur][jCur]
                        if n=='.':
                            continue
                        if visited[ord(n)-ord1]:
                            return False
                        visited[ord(n)-ord1]=True
                visited=[False]*9
        return True