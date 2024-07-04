#type: ignore
"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

 
Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.


Example 2:
Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.

Example 3:
Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
"""

from TreeNode import TreeNode

from typing import Optional


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        This is a DFS based solution. 

        Using a stack and track sum so far till the point a pop has to be done.
        When there is a sum that equals to targetSum
        """
        stack = []
        if root is None:
            return False
        p = root
        sum = 0
        visited = []
        while True:
            sum += p.val
            stack.append(p)
            visited.append(p)
            if p.left is None and p.right is None:
                # Reach a point that a pop has to be done
                if sum == targetSum:
                    return True
                targetSum -= p.val
                stack.pop()
                p = stack[-1]
            else:
                if p.left not in visited:
                    stack.append(p.left)
                    visited.append(p.left)
                    sum += p.left.val # type: ignore
                    p = p.left
                elif p.right not in visited:
                    stack.append(p.right)
                    visited.append(p.right)
                    sum += p.right.val # type: ignore
                    p = p.right
                else:
                    # need to pop now
                    if targetSum == sum:
                        return True
                    sum -= p.val
                    stack.pop()
                    p = stack[-1]
                
        return False