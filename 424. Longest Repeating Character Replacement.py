# [3/24/2024]Time up
# 38%/14%
""" 
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
 

Constraints:

1 <= s.length <= 10^5
s consists of only uppercase English letters.
0 <= k <= s.length
 """
from typing import Dict, List


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=len(s)
        iLeft=0  # Inclusive
        iRight=1  # Inclusive
        maxChar=s[0]
        maxCount=1
        restCharCounter:Dict[str,int]={}
        maxLength=1
        while iRight!=l:
            right=s[iRight]
            if right==maxChar:
                maxCount+=1
                maxLength=max(maxLength,iRight-iLeft+1)
                iRight+=1
                continue
            if right not in restCharCounter:
                restCharCounter[right]=0
            restCharCounter[right]+=1
            if maxCount<restCharCounter[right]:
                # swap
                restCharCounter[maxChar],maxChar,maxCount=maxCount,right,restCharCounter[right]
                restCharCounter.pop(maxChar)
            # restSum>k: move iLeft
            while sum(restCharCounter.values())>k:
                left=s[iLeft]
                if left==maxChar:
                    maxCount-=1
                    restMaxChar=max(restCharCounter, key=restCharCounter.get)
                    restMaxCount = restCharCounter[restMaxChar]
                    if maxCount<restMaxCount:
                        # swap
                        restCharCounter[maxChar],maxChar,maxCount=maxCount,restMaxChar,restMaxCount
                        restCharCounter.pop(maxChar)
                else:
                    if restCharCounter[left]==1:
                        restCharCounter.pop(left)
                    else:
                        restCharCounter[left]-=1
                iLeft+=1
            maxLength=max(maxLength,iRight-iLeft+1)
            iRight+=1
            continue

        return maxLength
            

