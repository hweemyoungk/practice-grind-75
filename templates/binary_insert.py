from typing import List


# Returns index for num to be inserted at.
# Array must already been sorted in ascending order.
def binary_insert(arr: List[int], num: int) -> int:
    # Corner case
    if len(arr) == 0:
        return 0
    
    left = 0  # Inclusive
    right = len(arr)  # Exclusive
    while left < right:
        mid = (left+right)//2
        medium = arr[mid]
        if num < medium:
            index = mid
            right = mid
            continue
        if medium < num:
            index = mid + 1
            left = mid + 1
            continue
        # Match: break
        index = mid
        break
    
    return index
