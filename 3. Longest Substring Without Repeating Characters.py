# [3/13/2024]19m out of 20m
# 95%
""" 
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 10^4
s consists of English letters, digits, symbols and spaces.
 """
from typing import List, Tuple


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)
        # Corner case
        if l<2:
            return l
        globalLongest = 1
        localCharIdx = {s[0]: 0}
        left = 0  # inclusive
        for right in range(1, l):  # inclusive
            c = s[right]
            if c in localCharIdx:
                # Repeat found
                localLongest = right-left
                globalLongest = max(localLongest, globalLongest)
                prevIdx = localCharIdx[c]
                for i in range(left, prevIdx+1):
                    localCharIdx.pop(s[i])
                localCharIdx[c]=right
                left = prevIdx+1
                continue
            # Not a repeat
            localLongest = right-left+1
            globalLongest = max(localLongest, globalLongest)
            localCharIdx[c]=right
        
        return globalLongest


    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     def binary_insert(arr: List[Tuple[int, str]], num: int) -> int:
    #         # Corner case
    #         if len(arr) == 0:
    #             return 0
            
    #         left = 0  # Inclusive
    #         right = len(arr)  # Exclusive
    #         while left < right:
    #             mid = (left+right)//2
    #             medium = arr[mid]
    #             if num < medium[0]:
    #                 index = mid
    #                 right = mid
    #                 continue
    #             if medium[0] < num:
    #                 index = mid + 1
    #                 left = mid + 1
    #                 continue
    #             # Match: break
    #             index = mid
    #             break
            
    #         return index

    #     l = len(s)
    #     # Corner case
    #     if l<2:
    #         return l
        
    #     globalLongest = 1

    #     localCharIdx = {s[0]: 0}
    #     # localIdxChar = {0: s[0]}
    #     localIdxChar = [(0, s[0])]
    #     start = 0  # Inclusive
    #     for i in range(1, len(s)):
    #         c = s[i]
    #         if c in localCharIdx:
    #             # Repeat found
    #             localLongest = i - start
    #             globalLongest = max(globalLongest, localLongest)
    #             # Set new start
    #             start = localCharIdx[c]+1
    #             # Remove entries before start
    #             index = binary_insert(localIdxChar, start)
    #             charsToRemove = localIdxChar[:index]
    #             [localCharIdx.pop(tup[1]) for tup in charsToRemove]
    #             localIdxChar = localIdxChar[index:]

    #             localCharIdx[c] = i
    #             localIdxChar.append((i, c))
    #             continue
            
    #         # Not a repeat
    #         localCharIdx[c] = i
    #         localIdxChar.append((i, c))
    #         localLongest = i - start + 1
    #         globalLongest = max(globalLongest, localLongest)
        
    #     return globalLongest