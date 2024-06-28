"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
 

Follow up: Could you solve it both recursively and iteratively?

"""

from TreeNode import TreeNode

from typing import Optional

class Solution:
    def isSymmetricRecursive(self, root: Optional[TreeNode]) -> bool:
        if root.left is None and root.right is None: # type: ignore
            return True
        if root.left is None and root.right is not None: # type: ignore
            return False
        if root.left is not None and root.right is None: # type: ignore
            return False
        if root.left.val != root.right.val: # type: ignore
            return False
        l = self.invertTree(root.left) # type: ignore
        print('left tree after invert - ')
        TreeNode.printTreeBFS(l)
        print('right tree -')
        TreeNode.printTreeBFS(root.right) # type: ignore
        return self.isSameTree(l, root.right) # type: ignore
    
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
    
    def isSameTree(
            self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p.val != q.val: # type: ignore
            return False
        return self.isSameTree(
            p.left, q.left) and self.isSameTree(p.right, q.right) # type: ignore
    

s = Solution()

print('TC#1')
rootarr = [1, 2, 2, 3, 4, 4, 3]
root = TreeNode.generateTreeFromBFS(rootarr)
print('Recursively - ', s.isSymmetricRecursive(root))

print('TC#2')
rootarr = [1, 2, 2, None, 3, None, 3]
root = TreeNode.generateTreeFromBFS(rootarr)
print('Recursively - ', s.isSymmetricRecursive(root))
