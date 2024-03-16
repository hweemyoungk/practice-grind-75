# [3/14/2024]18m out of 20m(90%)
# 21%/60%
# 23%/99%
""" 
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
 

Constraints:

-2^31 <= val <= 2^31 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 10^4 calls will be made to push, pop, top, and getMin.
 """
from typing import List


class MinStack:
    def __init__(self):
        self.stack: List[int] = []
        self.minStack: List[List[int]] = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minStack)==0:
            self.minStack.append([val, 1])
            return
        lastMinStackElement = self.minStack[len(self.minStack)-1]
        if val < lastMinStackElement[0]:
            self.minStack.append([val, 1])
            return
        # Equal or over min: Increment count
        lastMinStackElement[1]+=1

    def pop(self) -> None:
        val = self.stack.pop()
        lastMinStackElement = self.minStack[len(self.minStack)-1]
        if lastMinStackElement[1] == 1:
            # Remove frame
            self.minStack.pop()
            return
        # Decrement count
        lastMinStackElement[1]-=1
    

    def top(self) -> int:
        return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        return self.minStack[len(self.minStack)-1][0]

    # Binary search: O(n) where n is range of values
    # def __init__(self):
    #     self.stack = []
    #     self.sortedNums = []
    #     self.counters = []

    # def push(self, val: int) -> None:
    #     index = self.__binary_insert(self.sortedNums, val)
    #     if index != len(self.sortedNums) and self.sortedNums[index] == val:
    #         self.counters[index]+=1
    #     else:
    #         self.sortedNums.insert(index, val)
    #         self.counters.insert(index, 1)
    #     self.stack.append(val)
        

    # def pop(self) -> None:
    #     val = self.stack.pop()
    #     index = self.__binary_insert(self.sortedNums, val)
    #     self.counters[index]-=1
    #     if self.counters[index] == 0:
    #         # remove
    #         self.sortedNums.pop(index)
    #         self.counters.pop(index)
    #     return val
    

    # def top(self) -> int:
    #     return self.stack[len(self.stack)-1]

    # def getMin(self) -> int:
    #     return self.sortedNums[0]

    # def __binary_insert(self, arr: List[int], num: int) -> int:
    #     # Corner case
    #     if len(arr) == 0:
    #         return 0
        
    #     left = 0  # Inclusive
    #     right = len(arr)  # Exclusive
    #     while left < right:
    #         mid = (left+right)//2
    #         medium = arr[mid]
    #         if num < medium:
    #             index = mid
    #             right = mid
    #             continue
    #         if medium < num:
    #             index = mid + 1
    #             left = mid + 1
    #             continue
    #         # Match: break
    #         index = mid
    #         break
        
    #     return index
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()