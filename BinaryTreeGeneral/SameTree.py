"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false
 

Constraints:

The number of nodes in both trees is in the range [0, 100].
-10^4 <= Node.val <= 10^4

"""

from curses.ascii import SO
from TreeNode import TreeNode

from typing import Optional


class Solution:
    def isSameTree(
            self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p.val != q.val: # type: ignore
            return False
        return self.isSameTree(
            p.left, q.left) and self.isSameTree(p.right, q.right) # type: ignore
    

s = Solution()

parr = [1,2,3]
qarr = [1,2,3]
p = TreeNode.generateTreeFromBFS(parr)
q = TreeNode.generateTreeFromBFS(qarr)
print(s.isSameTree(p, q))

parr = [1,2]
qarr = [1,None,2]
p = TreeNode.generateTreeFromBFS(parr)
q = TreeNode.generateTreeFromBFS(qarr)
print(s.isSameTree(p, q))

parr = [1,2,1]
qarr = [1,1,2]
p = TreeNode.generateTreeFromBFS(parr)
q = TreeNode.generateTreeFromBFS(qarr)
print(s.isSameTree(p, q))
