"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

Example 3:
Input: root = [1,2], p = 1, q = 2
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 10^5].
* -10^9 <= Node.val <= 10^9
* All Node.val are unique.
* p != q
* p and q will exist in the tree
"""

from TreeNode import TreeNode
from typing import Optional

class Solution:
    def lowestCommonAncestor(
            self, 
            root: TreeNode, 
            p: TreeNode, 
            q: TreeNode) -> Optional[TreeNode]:
        # If the current node is null, return null
        if not root:
            return None
        
        # If the current node is either p or q, return the current node
        if root == p or root == q:
            return root
        
        # Recursively search for p and q in the left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q) # type: ignore
        right = self.lowestCommonAncestor(root.right, p, q) # type: ignore
        
        # If both left and right are non-null, the current node is the LCA
        if left and right:
            return root
        
        # Otherwise, return the non-null value
        return left if left else right