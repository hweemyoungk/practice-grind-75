from typing import List


# Returns index of num if found or complement of index for num to be inserted at.
# Array must already been sorted in ascending order.
def binary_search(arr: List[int], num: int) -> int:
    l = len(arr)
    # Corner case
    if l == 0:
        return ~0
    if l == 1:
        if num == arr[0]:
            return 0
        return ~0 if num < arr[0] else ~1
    
    lo = 0  # Inclusive
    hi = l-1  # Inclusive
    while lo <= hi:
        mid = (lo+hi+1)//2
        medium = arr[mid]
        if num < medium:
            index = mid-1
            hi = mid-1
            continue
        if medium < num:
            index = mid+1
            lo = mid+1
            continue
        # Match: break
        return mid
    # Not found
    if index==-1:
        return ~0
    # if index==l:
    #     return ~l
    return ~index
