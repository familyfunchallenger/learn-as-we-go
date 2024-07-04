"""
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:
Input: root = [1,null,3]
Output: [1,3]

Example 3:
Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""

from TreeNode import TreeNode
from typing import List, Optional


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        if not root:
            return ret
        q = [root]
        p = root
        while len(q) > 0:
            ret.append(q[0].val)
            q.pop(0)
            if p.right:
                p = p.right
                q.append(p)
            elif p.left:
                p = p.left
                q.append(p)
        return ret
    

s = Solution()

rarr = [1,2,3,None,5,None,4]
root = TreeNode.generateTreeFromBFS(rarr)
print(s.rightSideView(root))


rarr = [1,None,3]
root = TreeNode.generateTreeFromBFS(rarr)
print(s.rightSideView(root))


rarr = []
root = TreeNode.generateTreeFromBFS(rarr)
print(s.rightSideView(root))