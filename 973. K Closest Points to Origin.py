# [3/12/2024]10m out of 30m
# 33%
""" 
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

 

Example 1:


Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
 

Constraints:

1 <= k <= points.length <= 10^4
-10^4 <= xi, yi <= 10^4
 """
from typing import List, Tuple


class Solution:
    def pivotArray(self, arr: List[Tuple[int, List[int]]], k: int) -> Tuple[List[Tuple[int, List[int]]], List[Tuple[int, List[int]]]]:
        left = []
        right = []
        i=0
        while len(left) == 0:
            if i == len(arr):
                # All distances are same
                return arr[:k], []
            left = []
            right = []
            pivot = arr[i]
            for e in arr:
                if e[0] < pivot[0]:
                    left.append(e)
                    continue
                right.append(e)
            i+=1


        return (left, right)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        from random import Random
        self.random = Random()

        arr = [(point[0]**2 + point[1]**2, point) for point in points]

        closests = []

        # Randomly select a value and split array
        while 0 < k:
            if len(arr) == 1:
                closests.append(arr[0][1])
                break

            left, right = self.pivotArray(arr, k)
            if len(left) <= k:
                closests.extend([e[1] for e in left])
                k = k - len(left)
                arr = right
                continue
            # k < len(left)
            arr = left
            continue

        return closests