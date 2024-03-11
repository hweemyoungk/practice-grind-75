# [3/11/2024]18.5min
""" 
1 <= s.length <= 2 * 10^5
s consists only of printable ASCII characters.
 """
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            # Find valid char
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1

        return True
