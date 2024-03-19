from typing import List


# Returns index of num if found or complement of index for num to be inserted at.
# Array must already been sorted in ascending order.
def binary_search_rightmost(arr: List[int], target: int) -> int:
    l = len(arr)
    # Corner case
    if l == 0:
        return ~0
    if l == 1:
        if target == arr[0]:
            return 0
        return ~0 if target < arr[0] else ~1
    
    # exclusive lo
    # inclusive hi
    lo, hi = -1, len(arr)-1
    while lo < hi :
        m = (lo + hi + 1) // 2
        if target < arr[m]:
            hi = m - 1
        else: 
            lo = m
    if hi==-1:
        return -1
    if arr[(hi)]!=target:
        return ~(hi+1)
    return hi

print(binary_search_rightmost([-1,1,1,3,5],-2), ~0)
print(binary_search_rightmost([-1,1,1,3,5],0), ~1)
print(binary_search_rightmost([-1,1,1,3,5],1), 2)
print(binary_search_rightmost([-1,1,1,3,5],2), ~3)
print(binary_search_rightmost([-1,1,1,3,5],4), ~4)
print(binary_search_rightmost([-1,1,1,3,5],6), ~5)