"""
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

Example 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]


Example 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]
 

Constraints:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.
"""

from TreeNode import TreeNode

from typing import List, Optional


class Solution:
    def buildTree(
            self, 
            preorder: List[int], 
            inorder: List[int]) -> Optional[TreeNode]:
        # print('------------------')
        # print('preorder - ', preorder)
        # print('inorder - ', inorder)
        
        if len(preorder) != len(inorder) or len(preorder) == 0:
            print('invalid')
            return None
        if len(preorder) == 1:
            # print('leaf node - ', preorder[0] )
            # print('*****************')
            return TreeNode(preorder[0])
        head = TreeNode(preorder[0])
        
        
        index_of_head_within_inorder = inorder.index(preorder[0])
        size_of_left = index_of_head_within_inorder
        preorder_left = preorder[1:index_of_head_within_inorder + 1]
        inorder_left = inorder[0:index_of_head_within_inorder]
        # print('preorder_left - ', preorder_left)
        # print('inorder_left -  ', inorder_left)
        head.left = self.buildTree(preorder_left, inorder_left)
        
        size_of_right = len(preorder) - size_of_left
        preorder_right = preorder[-size_of_right + 1:]
        inorder_right = inorder[index_of_head_within_inorder + 1:]
        # print('preorder_right - ', preorder_right)
        # print('inorder_right -  ', inorder_right)
        head.right = self.buildTree(preorder_right, inorder_right)
        return head
    
s = Solution()

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
TreeNode.printTreeBFS(s.buildTree(preorder, inorder))

preorder = [-1]
inorder = [-1]