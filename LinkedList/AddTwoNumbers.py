"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

"""


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return '[val: {0}; next {1};]'.format(self.val, self.next)


class Solution:
    def _parseNumber(self, l: Optional[ListNode]) -> int:
        ret = 0
        power = 0
        while l is not None:
            ret = ret + l.val * (10 ** power)
            power += 1
            l = l.next 
        return ret
    
    def _generateList(self, n: int) -> Optional[ListNode]:
        if n == 0:
            return ListNode(0)
        head = None
        r = None
        while n != 0:
            m = n % 10
            n = n // 10
            p = ListNode(m)
            # print('p = ', p)
            if head is None:
                head = p
            if r is None:
                r = p
            else:
                r.next = p
                r = r.next
        print(head)
        return head

    def printList(self, l: Optional[ListNode]) -> None:
        if l is None:
            print('empty list')
            return
        ret = []
        while l is not None:
            ret.append(l.val)
            l = l.next
        print(ret)

    def addTwoNumbers(
            self, 
            l1: Optional[ListNode], 
            l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = self._parseNumber(l1)
        print('n1 = ', n1)
        n2 = self._parseNumber(l2)
        print('n2 = ', n2)
        return self._generateList(n1 + n2)
    

s = Solution()

# l1 = [2,4,3], l2 = [5,6,4]
l1a = ListNode(2)
l1b = ListNode(4)
l1c = ListNode(3)
l1a.next = l1b
l1b.next = l1c

l2a = ListNode(5)
l2b = ListNode(6)
l2c = ListNode(4)
l2a.next = l2b
l2b.next = l2c

l = s.addTwoNumbers(l1a, l2a)
s.printList(l)

# l1 = [0], l2 = [0]
l1a = ListNode(0)
l2a = ListNode(0) 
l = s.addTwoNumbers(l1a, l2a)
s.printList(l)

# l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
l1a = ListNode(9)
l1b = ListNode(9)
l1c = ListNode(9)
l1d = ListNode(9)
l1e = ListNode(9)
l1f = ListNode(9)
l1g = ListNode(9)
l1a.next = l1b
l1b.next = l1c
l1c.next = l1d
l1d.next = l1e
l1e.next = l1f
l1f.next = l1g

l2a = ListNode(9)
l2b = ListNode(9)
l2c = ListNode(9)
l2d = ListNode(9)
l2a.next = l2b
l2b.next = l2c
l2c.next = l2d

l = s.addTwoNumbers(l1a, l2a)
s.printList(l)