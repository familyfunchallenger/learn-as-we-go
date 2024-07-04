"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

 
Example 1:
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.


Example 2:
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
 

Constraints:

The number of nodes in the tree is in the range [1, 3 * 10^4].
-1000 <= Node.val <= 1000

"""

from math import inf
from TreeNode import TreeNode
from typing import Optional

class Solution:
    def __init__(self):
        self.max_sum = -float(inf)

    def maxPathSumWithWrongUnderstanding(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        max = 0
        stack = [root]
        visited = [root]
        current_num = root.val
        p = root
        while stack:
            if p.left is not None and p.left not in visited:
                p = p.left
                visited.append(p)
                stack.append(p)
                current_num = current_num + p.val
                # print('left is not none and not yet visited')
                # print('visited = ', visited)
                # print(current_num)
            elif p.right is not None and p.right not in visited:
                p = p.right
                visited.append(p)
                stack.append(p)
                current_num = current_num + p.val
                # print('left is not none and not yet visited')
                # print('visited = ', visited)
                # print(current_num)
            else:
                # both child nodes are None and/or visited
                if p.left is None and p.right is None:
                    print(current_num)
                    if current_num > max:
                        max = current_num
                current_num -= p.val
                stack.pop()
                if len(stack):
                    p = stack[-1]
                
        return max
    

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')
        
        def dfs(node):
            if not node:
                return 0
            
            # Recursively get the max path sum of the left and right subtrees
            left_max = max(dfs(node.left), 0)
            right_max = max(dfs(node.right), 0)
            
            # Calculate the path sum passing through the current node
            current_sum = node.val + left_max + right_max
            
            # Update the global maximum path sum if the current path sum is greater
            self.max_sum = max(self.max_sum, current_sum)
            
            # Return the maximum path sum starting from the current node
            return node.val + max(left_max, right_max)
        
        dfs(root)
        return self.max_sum # type: ignore
    

s = Solution()

rarr = [1,2,3]
root = TreeNode.generateTreeFromBFS(rarr)
print(s.maxPathSum(root))
#print(s.maxPathSumWithWrongUnderstanding(root))

rarr = [-10,9,20,None,None,15,7]
root = TreeNode.generateTreeFromBFS(rarr)
print(s.maxPathSum(root))
#print(s.maxPathSumWithWrongUnderstanding(root))
