# [3/11/2024]15.5 min
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        openings = pairs.values()
        for char in s:
            # Opening
            if char in openings:
                stack.append(char)
                continue
            # Closing: s consists of parentheses only '()[]{}'.
            try:
                if stack.pop() != pairs[char]:
                    return False
            except:
                return False
        return len(stack) == 0

if __name__ == "__main__":
    Solution().isValid("()")