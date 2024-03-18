# [3/18/2024]Retire
""" 
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
 """
from collections import deque
from typing import Dict, List, Optional, Tuple


class LRUCache:

    # Linked list
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.size=0
        self.head=None
        self.tail=None
        self.nodes: Dict[int, DoublyLinkedNode]={}
    
    def __toTail(self, node: 'DoublyLinkedNode'):
        if node==self.tail:
            return
        if node==self.head:
            self.head=node.next
        else:
            node.prev=node.next
        node.next=None
        self.tail.next=node
        self.tail=node
        return

    def get(self, key: int) -> int:
        if key in self.nodes:
            node = self.nodes[key]
            self.__toTail(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            node = self.nodes[key]
            node.val=value
            self.__toTail(node)
            return
        
        # Not found
        if self.size==self.capacity:
            # Deque
            head=self.head
            self.head=head.next
            self.nodes.pop(head.key)
            self.size-=1
        
        node=DoublyLinkedNode(key, value)
        self.nodes[key]=node
        if self.size==0:
            # Empty
            self.head=node
            self.tail=node
            self.size+=1
            return
        # Append
        self.tail.next=node
        self.tail=node
        self.size+=1
        return

class DoublyLinkedNode:
    def __init__(self, key: int, val: int, prev: Optional['DoublyLinkedNode']=None, next: Optional['DoublyLinkedNode']=None) -> None:
        self.key=key
        self.val=val
        self.prev=prev
        self.next=next

    # Array: Time exceeded
    """ 
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.keys: List[Optional[int]]=[None]*capacity
        self.values: List[Optional[int]]=[None]*capacity

    def get(self, key: int) -> int:
        try:
            index = self.keys.index(key)
            value = self.values[index]
        except:
            # Not found
            return -1
        # Found
        while index!=self.capacity-1:
            # Shift
            iNext=(index+1)%self.capacity
            self.keys[index]=self.keys[iNext]
            self.values[index]=self.values[iNext]
            index=iNext
        # index==self.capacity-1
        self.keys[index]=key
        self.values[index]=value
        return value

    def put(self, key: int, value: int) -> None:
        try:
            index = self.keys.index(key)
        except:
            # Not found
            self.keys[0]=key
            self.values[0]=value
            self.get(key)
            return
        # Found
        self.values[index]=value
        self.get(key)
        """

    # Heap: Time exceeded
    """
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.size=0
        self.cache: List[Tuple[int, Tuple[int,int]]] =[]
        self.priority=0

    def get(self, key: int) -> int:
        for i, (_, kv) in enumerate(self.cache):
            if key==kv[0]:
                # Replace
                self.cache[i] = self.cache[-1]
                self.cache.pop()
                self.size-=1
                heapq.heapify(self.cache)
                heapq.heappush(self.cache, (self.priority, kv))
                self.priority+=1
                self.size+=1
                return kv[1]
        return -1

    def put(self, key: int, value: int) -> None:
        for i, (_, kv) in enumerate(self.cache):
            if key==kv[0]:
                # Replace
                self.cache[i] = self.cache[-1]
                self.cache.pop()
                self.size-=1
                heapq.heapify(self.cache)
                heapq.heappush(self.cache, (self.priority, (key, value)))
                self.priority+=1
                self.size+=1
                return

        # Not found
        if self.size==self.capacity:
            # Pop least priority
            heapq.heappop(self.cache)
            self.size-=1
        
        # Add to cache
        heapq.heappush(self.cache, (self.priority, (key, value)))
        self.priority+=1
        self.size+=1
        return
    """
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)