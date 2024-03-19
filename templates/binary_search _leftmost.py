from typing import List


# Returns index of num if found or complement of index for num to be inserted at.
# Array must already been sorted in ascending order.
def binary_search_leftmost(arr: List[int], target: int) -> int:
    l = len(arr)
    # Corner case
    if l == 0:
        return ~0
    if l == 1:
        if target == arr[0]:
            return 0
        return ~0 if target < arr[0] else ~1
    
    lo, hi = 0, len(arr)
    while lo < hi :
        m = (lo + hi) // 2
        if arr[m] < target:
            lo = m + 1
        else: 
            hi = m
    if lo==l:
        return ~l
    if arr[lo]!=target:
        return ~lo
    return lo

print(binary_search_leftmost([-1,1,1,3,5],-2), ~0)
print(binary_search_leftmost([-1,1,1,3,5],0), ~1)
print(binary_search_leftmost([-1,1,1,3,5],1), 1)
print(binary_search_leftmost([-1,1,1,3,5],2), ~3)
print(binary_search_leftmost([-1,1,1,3,5],4), ~4)
print(binary_search_leftmost([-1,1,1,3,5],6), ~5)