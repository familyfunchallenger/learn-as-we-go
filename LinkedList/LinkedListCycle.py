"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).


Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.


Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
 

Constraints:

The number of the nodes in the list is in the range [0, 10^4].
-10^5 <= Node.val <= 10^5
pos is -1 or a valid index in the linked-list.
 

Follow up: Can you solve it using O(1) (i.e. constant) memory?
"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        # Now we have more than one node in the singly linked list
        normal_speed = head
        double_speed = head.next
        while normal_speed != double_speed:
            # move normal speed pointer one element donw
            if normal_speed != None:
                normal_speed = normal_speed.next
            if double_speed != None:
                double_speed = double_speed.next
            if double_speed != None:
                double_speed = double_speed.next
        if normal_speed is None and double_speed is None:
            return False
        return True
    

s = Solution()

# head = [3,2,0,-4]
listNode1 = ListNode(3)
listNode2 = ListNode(2)
listNode3 = ListNode(0)
listNode4 = ListNode(-4)
listNode1.next = listNode2  # type: ignore
listNode2.next = listNode3  # type: ignore
listNode3.next = listNode4  # type: ignore
listNode4.next = listNode2  # type: ignore
print(s.hasCycle(listNode1))


# head = [1,2]
listNode1 = ListNode(1)
listNode2 = ListNode(2)
listNode1.next = listNode2  # type: ignore
listNode2.next = listNode1  # type: ignore
print(s.hasCycle(listNode1))


# head = [1]
listNode1 = ListNode(1)
print(s.hasCycle(listNode1))

