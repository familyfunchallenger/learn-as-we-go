"""

Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

Example 1:
Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: inorder = [-1], postorder = [-1]
Output: [-1]
 

Constraints:

1 <= inorder.length <= 3000
postorder.length == inorder.length
-3000 <= inorder[i], postorder[i] <= 3000
inorder and postorder consist of unique values.
Each value of postorder also appears in inorder.
inorder is guaranteed to be the inorder traversal of the tree.
postorder is guaranteed to be the postorder traversal of the tree.
"""

from TreeNode import TreeNode

from typing import List, Optional

class Solution:
    def buildTree(
            self,
            inorder: List[int],
            postorder: List[int]) -> Optional[TreeNode]:
        if (inorder is None and postorder is None) or (
            len(inorder) != len(postorder)) or len(inorder) == 0:
            return None
        root_val = postorder[-1]
        head = TreeNode(root_val)
        if len(inorder) == 1:
            return head

        size_of_left = inorder.index(root_val)
        size_of_right = len(inorder) - size_of_left - 1

        in_left = inorder[0:size_of_left]
        post_left = postorder[0:size_of_left]
        head.left = self.buildTree(in_left, post_left)

        in_right = inorder[size_of_left + 1:]
        post_right = postorder[size_of_left: -1]
        # print('in_right: ', in_right)
        # print('post_right: ', post_right)
        head.right = self.buildTree(in_right, post_right)
        return head
    

s = Solution()

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
TreeNode.printTreeBFS(s.buildTree(inorder, postorder))

inorder = [-1]
postorder = [-1]
TreeNode.printTreeBFS(s.buildTree(inorder, postorder))
