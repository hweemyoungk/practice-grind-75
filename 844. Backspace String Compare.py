# [3/11/2024]Time up: 19m out of 15m
""" 
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
 

Constraints:

1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.
 

Follow up: Can you solve it in O(n) time and O(1) space?
 """
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sBackspaceStack = 0
        tBackspaceStack = 0
        i=len(s) - 1
        j=len(t) - 1
        while i > -1 or j > -1:
            c = s[i] if i > -1 else ""
            d = t[j] if j > -1 else ""
            if c == "#":
                sBackspaceStack+=1
                i-=1
                continue
            if d == "#":
                tBackspaceStack+=1
                j-=1
                continue
            # Both are alpha chars
            if sBackspaceStack != 0:
                sBackspaceStack-=1
                i-=1
                continue
            if tBackspaceStack != 0:
                tBackspaceStack-=1
                j-=1
                continue
            # Both cannot be removed
            if c != d:
                return False
            # Both are same chars
            i-=1
            j-=1
        return True

