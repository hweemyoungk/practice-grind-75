# [3/19/2024]Time up
# 27%/6%
""" 
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique

 

Example 1:

Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.
Example 2:

Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.

Constraints:

n == gas.length == cost.length
1 <= n <= 10^5
0 <= gas[i], cost[i] <= 10^4
 """
from collections import deque
from typing import List, Tuple


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n=len(gas)
        nets=[0]*n
        iFirstPositive=None
        iLastNonPositive=None
        sum=0
        for i, (g,c) in enumerate(zip(gas,cost)):
            net=g-c
            sum+=net
            if net<=0:
                iLastNonPositive=i
            else:
                if iFirstPositive == None:
                    iFirstPositive=i
            nets[i]=net
        if sum<0:
            return-1
        if iFirstPositive!=None and iLastNonPositive==None:
            # Can travel
            return iFirstPositive
        if iFirstPositive==None and iLastNonPositive!=None:
            if sum==0:
                # Still can travel... from i=0 maybe?
                return 0
            # Cannot travel
            return -1
        
        if iLastNonPositive==n-1 and iFirstPositive!=0:
            start=iFirstPositive
        else:
            start=(iLastNonPositive+1)%n
        
        queue = deque(nets[start:] + nets[:start])
        blocks: List[Tuple[int,int]]=[]
        blockSum=0
        count=0
        while queue:
            curr = queue.popleft()
            count+=1
            blockSum+=curr
            if curr<0:
                # Peek next is also negative
                if queue and queue[0]<0:
                    continue
                # Non-negative or empty: end the block
                blocks.append((start, blockSum))
                start=(start+count)%n
                blockSum=0
                count=0
        
        # Find max block
        iMaxBlockSum=None
        maxBlockSum=0
        for i,(start, blockSum) in enumerate(blocks):
            if blockSum<maxBlockSum:
                continue
            iMaxBlockSum=i
            maxBlockSum=blockSum
        # Try travel
        sum=0
        iCandidate = blocks[iMaxBlockSum][0]
        for _, blockSum in blocks[iMaxBlockSum:]+blocks[:iMaxBlockSum]:
            sum+=blockSum
            if sum<0:
                return -1
        return iCandidate