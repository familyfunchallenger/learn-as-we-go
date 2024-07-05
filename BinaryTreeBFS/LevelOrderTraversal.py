"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example 1:
Input: root = [3,9,20,None,None,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000

"""

from TreeNode import TreeNode
from typing import List, Optional


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret = []
        if not root:
            return ret
        current_lvl = 0
        lvls = {}
        lvls[0] = [root]
        all_leaves = False
        ret.append([root.val])
        while not all_leaves:
            # based on nodes in current_lvl, fill the nodes at current_lvl + 1
            next_level = []
            for n in lvls[current_lvl]:
                if n.left:
                    next_level.append(n.left)
                if n.right:
                    next_level.append(n.right)
            if len(next_level) == 0:
                all_leaves = True
            else:
                current_lvl += 1
                lvls[current_lvl] = next_level
                ret.append([node.val for node in next_level])
        return ret
    

s = Solution()

rarr = [3,9,20,None,None,15,7]
root = TreeNode.generateTreeFromBFS(rarr)
print(s.levelOrder(root))

rarr = [1]
root = TreeNode.generateTreeFromBFS(rarr)
print(s.levelOrder(root))

rarr = []
root = TreeNode.generateTreeFromBFS(rarr)
print(s.levelOrder(root))

