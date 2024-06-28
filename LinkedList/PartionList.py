"""
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example 1:
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]


Example 2:
Input: head = [2,1], x = 2
Output: [1,2]
 

Constraints:

The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200
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
    def partition(self, 
                  head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """
        Use two linked list to construct the before and after lists, then concatenate them
        """
        if head is None or head.next is None:
            return head
        less_list_dummy_node = ListNode(-1)
        other_list_dummy_node = ListNode(-1)
        hl = less_list_dummy_node
        hge = other_list_dummy_node
        while head is not None:
            if head.val < x:
                # add this node to the less_list_dummy_node list
                hl.next = head
                if hl.next is not None:
                    hl = hl.next
            else:
                # add this node to the other_list_dummy_node list
                hge.next = head
                if hge.next is not None:
                    hge = hge.next
            head = head.next
        # now point hl.next to the hge.next
        hl.next = other_list_dummy_node.next
        hge.next = None
        return less_list_dummy_node.next
    

s = Solution()

# head = [1,4,3,2,5,2], x = 3
head = generateList([1, 4, 3, 2, 5, 2])
x = 3
print(s.partition(head, x))

# head = [2,1], x = 2
head = generateList([2, 1])
x = 2
print(s.partition(head, x))