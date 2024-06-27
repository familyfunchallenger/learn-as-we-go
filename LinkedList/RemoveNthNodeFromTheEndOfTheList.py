"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 
Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 

Follow up: Could you do this in one pass?
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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Two pointers
        both start from the head
        move the first pointer N steps down the line,
          if the first pointer reaches the end of the list before finishing N steps, cannot remove anything, return the original list
          if the first pointer is at the end of the list (i.e. the first pointer becomes None) after finishing the N-th move, it is to remove the 1st node
        now move both the first and the second pointers down the list till the second pointer's next is None. Then remove the first pointer's next
        """
        i = 0
        p = head
        p1 = head
        while i < n and p is not None:
            p = p.next
            i += 1
        if i < n:
            return head
        if i == n and p is None:
            # Need to remove head
            head = head.next  # type: ignore
            # need to free the space, ignored for now
            return head
        while p.next is not None:  # type: ignore
            p = p.next # type: ignore
            p1 = p1.next # type: ignore
        p1.next = p1.next.next  # type: ignore
        # ignore memory space free up
        return head
    

s = Solution()

# head = [1,2,3,4,5], n = 2
head = generateList([1,2,3,4,5])
n = 2
print(s.removeNthFromEnd(head, n))