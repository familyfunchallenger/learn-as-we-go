"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""

from re import L
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return '[val: {0}; next {1}]'.format(self.val, self.next)
    
    def printList(self) -> None:
        l = self.next
        ret = [self.val]
        while l is not None:
            ret.append(l.val)
            l = l.next
        print(ret)

    
def generateList(nums):
    h = None
    r = h
    if nums is None or len(nums) == 0:
        return h
    else:
        for n in nums:
            p = ListNode(n)
            if h is None:
                h = p
                r = p
            else:
                r.next = p
                r = p
    return h
        

class Solution:
    def mergeTwoLists(
            self, 
            list1: Optional[ListNode], 
            list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        # At this point, list1 and list2 are both valid
        h = None
        t = None
        h1 = list1
        h2 = list2
        while h1 is not None and h2 is not None:
            # print()
            # print('h => ', h)
            # print('t => ', t)
            # print('h1 => ', h1)
            # print('h2 => ', h2)
            if h is None:
                if h1.val < h2.val:
                    h = h1
                else:
                    h = h2
                    
            if h1.val < h2.val:
                if t is None:
                    t = h1
                else:
                    t.next = h1
                    t = h1
                h1 = h1.next
                # print('after h1.val < h2.val => ')
                # print('h => ', h)
                # print('t => ', t)
                # print('h1 => ', h1)
                # print('h2 => ', h2)
            else:
                if t is None:
                    t = h2
                else:
                    t.next = h2
                    t = h2
                h2 = h2.next
                # print('after h1.val >= h2.val => ')
                # print('h => ', h)
                # print('t => ', t)
                # print('h1 => ', h1)
                # print('h2 => ', h2)
        return h
    

s = Solution()

# list1 = [1,2,4], list2 = [1,3,4]
list1 = generateList([1, 2, 4])
list2 = generateList([1, 3, 4])
l = s.mergeTwoLists(list1, list2)
print(l)


# list1 = [], list2 = []
list1 = generateList([])
list2 = generateList([])
l = s.mergeTwoLists(list1, list2)
print(l)

# list1 = [], list2 = [0]
list1 = generateList([])
list2 = generateList([0])
l = s.mergeTwoLists(list1, list2)
print(l)