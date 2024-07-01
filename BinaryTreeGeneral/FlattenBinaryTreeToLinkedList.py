"""
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.
 

Example 1:
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [0]
Output: [0]
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
 

Follow up: Can you flatten the tree in-place (with O(1) extra space)?

"""

from TreeNode import TreeNode

from typing import List, Optional


class Solution:
    
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.

        With O(n) space, it should be straight forward by maintaining a list of the pre-order traverse result and then rebuild the tree by connecting the nodes according to the order in the list and the rule.

        If it is for O(1) space, it becomes somthing tricky
        """
        current = root
        while current:
            if current.left:
                # Find the rightmost node in the left subtree
                rightmost = current.left
                while rightmost.right:
                    rightmost = rightmost.right
                
                # Link the rightmost node's right to the current node's right
                rightmost.right = current.right
                
                # Move the left subtree to the right
                current.right = current.left
                current.left = None
            
            # Move to the next right node
            current = current.right