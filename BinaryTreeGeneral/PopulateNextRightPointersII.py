"""
Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Example 1:
Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

Example 2:
Input: root = []
Output: []
 

Constraints:
The number of nodes in the tree is in the range [0, 6000].
-100 <= Node.val <= 100
 
Follow-up:
* You may only use constant extra space.
* The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.

"""

from typing import List, Optional

class Node:
    def __init__(
            self, 
            val: int = 0, 
            left: 'Optional[Node]' = None,
            right: 'Optional[Node]' = None,
            next: 'Optional[Node]' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    @staticmethod
    def generateTreeFromBFS(arr: Optional[List[int]]) -> 'Optional[Node]':
        if arr is None:
            return None
        if len(arr) == 0:
            return None
        head = Node(arr[0])
        if len(arr) == 1:
            return head
        nodes = {}
        nodes[0] = head
        i = 0
        while i < len(arr):
            l = 2 * i + 1
            if l < len(arr):
                n = Node(arr[l])
                nodes[i].left = n
                nodes[l] = n
            if l + 1 < len(arr):
                n = Node(arr[l + 1])
                nodes[i].right = n
                nodes[l + 1] = n
            i += 1
        return head


class Solution:
    def connect(self, root: Optional[Node]) -> 'Node':
        """
        At high level, it is a BFS, the key is to be able to stop
        at the end of each level
        """
        if root is None:
            return None # type: ignore
        h = root
        narr = [h.val]

        i = 0
        levels = {}
        levels[0] = []
        while True:
            if i == 0:
                levels[i].append(h)
                h.next = None
            else:
                if i not in levels:
                    levels[i] = []
                prev_level = levels[i-1]
                j = 0
                while j < len(prev_level) - 2:
                    if prev_level[j].left is not None:
                        levels[i].append(prev_level[j].left)
                    if prev_level[j].rigth is not None:
                        levels[i].append(prev_level[j].right)
                    prev_level[j].next = prev_level[j + 1]
                    j += 1
                if prev_level[j].left is not None:
                        levels[i].append(prev_level[j].left)
                if prev_level[j].rigth is not None:
                    levels[i].append(prev_level[j].right)
                prev_level[j].next = None
                if levels[i] == 0:
                    break
            i += 1
        # Now we have the dict of each level, printing the output is straightforward
        return root