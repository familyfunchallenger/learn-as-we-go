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
 

Constraints:

1 <= capacity <= 3000
0 <= key <= 10^4
0 <= value <= 10^5
At most 2 * 10^5 calls will be made to get and put.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self) -> str:
        return '[key: {0}; val: {1}; next {2}; prev {3}]'.format(
            self.key, self.val, id(self.next), id(self.prev))
    
    def printList(self) -> None:
        l = self.next
        ret = [self.val]
        while l is not None:
            ret.append(l.val)
            l = l.next
        print(ret)



class LRUCache:

    def __init__(self, capacity: int):
        """
        maintain a linked list for the key - value retrieve
        each node has (key, val, next)
        if a node is accessed (get/put), it should be moved to the end of the list
        """
        self.capacity = capacity
        self.size = 0
        self.cache_container = ListNode(
            None, None, None, None)  # type: ignore
        self.cache_container_end = ListNode(
            None, None, None, None)  # type: ignore
        self.cache_container.next = self.cache_container_end
        self.cache_container_end.prev = self.cache_container

    def get(self, key: int) -> int:
        ret = 0
        h = self.cache_container
        while h is not None:
            if h.key == key:
                ret = h.val
                # remove this h from current position
                h.prev.next = h.next # type: ignore
                h.next.prev = h.prev # type: ignore
                # put this h ahead of the tail
                self.cache_container_end.prev.next = h # type: ignore
                h.next = self.cache_container_end
                self.cache_container_end.prev = h
                break

        return ret
        

    def put(self, key: int, value: int) -> None:
        return
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)