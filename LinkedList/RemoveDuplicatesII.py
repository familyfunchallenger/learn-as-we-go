"""
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.


Example 1:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:
Input: head = [1,1,1,2,3]
Output: [2,3]
 

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.

"""

from typing import Optional

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
                r.next = p # type: ignore
                r = p
    return h

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Solution should be straight forward:
            - having a pointer traversing the list from the head towards the end of the list in a loop 
                * if current node's val is the same as the next node's val, remove next node
                * if current node's val is different form the next node's val, move the pointer downwards one node
        """
        if head is None or head.next is None:
            return head
        p = head
        while p is not None:
            p1 = p.next
            if p1 is None:
                break
            if p.val == p1.val:
                # we can remove p1
                p.next = p1.next
                p1.next = None
                del p1
            else:
                p = p.next
        return head
    

s = Solution()

# head = [1,2,3,3,4,4,5]
head = generateList([1, 2, 3, 3, 4, 4, 5])
print(s.deleteDuplicates(head))