"""
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

Example 1:
Input: root = [4,2,6,1,3]
Output: 1

Example 2:
Input: root = [1,0,48,None,None,12,49]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 10^4].
0 <= Node.val <= 10^5
 

Note: This question is the same as 783: https://leetcode.com/problems/minimum-distance-between-bst-nodes/


"""

from TreeNode import TreeNode
from typing import Optional
import math

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        """
        The min difference must occur between two adjacent nodes, i.e. a parent node and a child node. Thus it is straigthforward to kee a record of current min diff while traverse all the nodes to get the difference between current node and its child node(s) and update the current min diff as needed
        """
        current_min = math.inf
        if not root:
            return 0
        p = root
        q = [root]
        while len(q) > 0:
            p = q[0]
            # print('value of queue head: ', p)
            if p.left:
                q.append(p.left)
                current_min = min(abs(p.val - p.left.val), current_min)
            if p.right:
                q.append(p.right)
                current_min = min(abs(p.val - p.right.val), current_min)
            q.pop(0)
        return current_min # type: ignore
    

s = Solution()

rarr = [4,2,6,1,3]
root = TreeNode.generateTreeFromBFS(rarr)
print(s.getMinimumDifference(root))

rarr = [1,0,48,None,None,12,49]
root = TreeNode.generateTreeFromBFS(rarr)
print(s.getMinimumDifference(root))
