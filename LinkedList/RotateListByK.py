"""
Given the head of a linked list, rotate the list to the right by k places.


Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]


Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]
 

Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 10^9
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
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        It is similar to remove the n-th node from the list.
        Need to identify the pointer to the (k % len(list))-th node in the list
        Then make
         - Head pointer to this particular node
         - The previous node's next to None
         - The original last element's next to the original head 
        """
        # Find out how long the linked list is
        length = 0
        if head is None:
            return None
        p = head
        while p is not None:
            length += 1
            p = p.next
         #print('length - ', length)
        if length == 1:
            # only one node, does not matter what the k's value is
            return head
        n = length % k + 1
        # print(' actual k (n) -> ', n)
        i = 0
        p = head
        p1 = head
        # print('head - ', str(head))
        while i < n and p is not None:
            p = p.next
            i += 1
            # print('p - ', str(p))
        if i < n:
            return head
        if p is None:
            return head
        while p.next is not None:  # type: ignore
            p = p.next # type: ignore
            p1 = p1.next # type: ignore
            # print('p - ', p)
            # print('p1 - ', p1)
        # p1 is not pointing to the node prev to the new head
        p.next = head    # type: ignore
        head = p1.next   # type: ignore
        p1.next = None  # type: ignore
        # ignore memory space free up
        return head
    

s = Solution()

# head = [1,2,3,4,5], k = 2
head = generateList([1, 2, 3, 4, 5])
print(s.rotateRight(head, 2))