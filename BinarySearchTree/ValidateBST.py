"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 
Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,None,None,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 

Constraints:

The number of nodes in the tree is in the range [1, 10^4].
-2^31 <= Node.val <= 2^31 - 1

"""

from TreeNode import TreeNode
from typing import Optional
import math

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        a tree is a valid BST if and only if the root at any level is larger than all the nodes on its left sub-tree and is less than all the nodes
        on its right sub-tree
        """

        def largestAndLeastInTheTree(node: TreeNode) -> tuple[int, int]:
            if not node:
                return -math.inf, math.inf  # type: ignore
            current_max = 0
            current_min = math.inf
            p = node
            q = [p]
            while q:
                p = q.pop()
                if p.val >= current_max:
                    current_max = p.val
                if p.val < current_min:
                    current_min = p.val
                if p.right:
                    q.append(p.right)
                if p.left:
                    q.append(p.left)
            print('current max and min: ', current_max, current_min)
            return (current_max, current_min) # type: ignore
        
        if not root:
            return True
        
        left_max, _ = largestAndLeastInTheTree(root.left) # type: ignore
        _, right_min = largestAndLeastInTheTree(root.right) # type: ignore
        return (left_max <= root.val and right_min >= root.val
                and self.isValidBST(root.right) 
                and self.isValidBST(root.left))
    

s = Solution()

rarr = [2,1,3]
root = TreeNode.generateTreeFromBFS(rarr)
print(s.isValidBST(root))

rarr= [5,1,4,None,None,3,6]
root = TreeNode.generateTreeFromBFS(rarr)
print(s.isValidBST(root))
