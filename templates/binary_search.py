from typing import List

from templates.binary_insert import binary_insert

# Returns index of target or -1 if not found.
# Array must already been sorted in ascending order.
# Very similar to binary insert.
# Get index using binary insert and check arr[index] matches target
def binary_search(arr: List[int], target: int) -> int:
    if len(arr) == 0:
        return -1
    
    index = binary_insert(arr, target)
    if index == len(arr):
        # Out of range
        return -1
    if target != arr[index]:
        # Not exists
        return -1
    
    return index
    