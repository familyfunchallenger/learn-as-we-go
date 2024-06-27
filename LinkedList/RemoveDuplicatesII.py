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

        above solution does not fully solve the problem. An easier way is to have a separate list to store only unique nodes.
        """
        if head is None or head.next is None:
            return head
        p = head
        p1 = p.next
        p2 = None
        val_of_dup = None
        while p is not None and p1 is not None:
            p2 = p1.next
            if p.val == p1.val or p.val == val_of_dup:
                # we can remove p1, p
                val_of_dup = p.val
                if p == head:
                    head = p.next # type: ignore
                    p = head
                else:
                    p.next = p1.next
                    p1.next = None
                #     del p1
            else:
                p = p.next
                val_of_dup = None
        return head
    
    def deleteDuplicates(head):
        # Create a dummy node to handle edge cases
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = head
        
        while current:
            # Skip all duplicates
            if current.next and current.val == current.next.val: # type: ignore
                # Move current until the end of duplicates sublist
                while current.next and current.val == current.next.val: # type: ignore
                    current = current.next # type: ignore
                # Skip all duplicates
                prev.next = current.next # type: ignore
            else:
                # No duplicates, move prev to current
                prev = prev.next # type: ignore
            # Move current forward
            current = current.next # type: ignore
        
        return dummy.next
        

s = Solution()

# head = [1,2,3,3,4,4,5]
head = generateList([1, 2, 3, 3, 4, 4, 5])
print(s.deleteDuplicates(head))