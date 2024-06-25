"""
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.

 

Example 1:
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Example 2:
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

Example 3:
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
 

Constraints:

0 <= n <= 1000
-10^4 <= Node.val <= 10^4
Node.random is null or is pointing to some node in the linked list.
"""

from typing import Optional

# Definition for a Node.
class Node:
    def __init__(
            self, 
            val: int, 
            next: 'Node' = None, # type: ignore
            random: 'Node' = None): # type: ignore
        self.val = int(val)
        self.next = next
        self.random = random

    def __str__(self) -> str:
        return '[id {0} - val {1} - next {2}] - random {3}'.format(
            id(self), self.val, id(self.next), id(self.random))
    
    def printList(self) -> None:
        l = self.next
        ret = [str(self)]
        while l is not None:
            ret.append(str(l))
            l = l.next
        print(ret)

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        Maintain a map of the node between the original and the copy

        two passes of the traversing the original (and target) lists:
        (1) one to construct the new target list and the mapping, and leave the random pointer alone
        (2) the next to use the map to construct the random field in the new list
        """
        if head is None:
            return None
        p = head
        new_head = None
        new_p = None
        nodes_mapping = {}
        nodes_mapping[None] = None
        while p is not None:
            # first pass
            n = Node(p.val)
            if new_head is None:
                new_head = n
                new_p = n
            else:
                new_p.next = n # type: ignore
                new_p = n
            nodes_mapping[p] = n
            p = p.next
        p = head
        new_p = new_head
        while p is not None:
            new_p.random = nodes_mapping[p.random] # type: ignore
            p = p.next
            new_p = new_p.next # type: ignore
        return new_head # type: ignore
    

s = Solution()


# head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
n1 = Node(7)
n2 = Node(13)
n3 = Node(11)
n4 = Node(10)
n5 = Node(1)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n1.random = None # type: ignore
n2.random = n1
n3.random = n4
n4.random = n2
n5.random = n1
n1.printList()
l = s.copyRandomList(n1)
l.printList() # type: ignore

# head = [[1,1],[2,1]]

# head = [[3,null],[3,0],[3,null]]

