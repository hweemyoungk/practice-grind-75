# [3/15/2024]11m out of 35m
# 81%/99%
""" 
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
 

Example 1:

Input
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output
[null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
timeMap.get("foo", 1);         // return "bar"
timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
timeMap.get("foo", 4);         // return "bar2"
timeMap.get("foo", 5);         // return "bar2"
 

Constraints:

1 <= key.length, value.length <= 100
key and value consist of lowercase English letters and digits.
1 <= timestamp <= 10^7
All the timestamps timestamp of set are strictly increasing.
At most 2 * 10^5 calls will be made to set and get.
 """
from typing import Dict, List, Tuple


class TimeMap:
    # Returns index of num if found or complement of index for num to be inserted at.
    # Array must already been sorted in ascending order.
    def __binary_search(self, arr: List[int], num: int) -> int:
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


    def __init__(self):
        self.d: Dict[str, Tuple[List[int], List[str]]] = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = ([], [])
        timestamps, values = self.d[key]
        # Do not binary search: All the timestamps timestamp of set are strictly increasing.
        # index = self.__binary_search(timestamps, timestamp)
        # if index<0:
        #     timestamps.insert(~index, timestamp)
        #     values.insert(~index, value)
        #     return
        # # Match found
        # timestamps[index]=timestamp
        # values[index]=value
        timestamps.append(timestamp)
        values.append(value)
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        timestamps, values = self.d[key]
        index = self.__binary_search(timestamps, timestamp)
        if index<0:
            # Check prev
            iPrev = ~index-1
            if iPrev<0:
                # No prev
                return ""
            return values[iPrev]
        return values[index]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)