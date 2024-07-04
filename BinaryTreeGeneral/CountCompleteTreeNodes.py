"""
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.

Example 1:
Input: root = [1,2,3,4,5,6]
Output: 6

Example 2:
Input: root = []
Output: 0

Example 3:
Input: root = [1]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [0, 5 * 10^4].
0 <= Node.val <= 5 * 10^4
The tree is guaranteed to be complete.


Approach
Height Calculation: Calculate the height of the left-most path, which gives us the height h of the tree. 

Binary Search on Last Level: Use binary search to determine how many nodes exist on the last level. Since all levels except the last are completely filled, we only need to check the last level to find the total number of nodes.

Total Nodes Calculation: Calculate the total number of nodes based on the number of nodes in the last level.

Detailed Steps
Calculate Tree Height: Traverse the left-most path of the tree to determine the height.

Binary Search for Last Level Nodes: Perform binary search to count nodes in the last level by checking the existence of nodes using the tree height.

Combine Results: Calculate the total number of nodes using the formula for the sum of nodes in a complete binary tree up to the second last level plus the nodes in the last level.

Explanation
Height Calculation: The get_height function calculates the height of the tree by traversing the left-most path. This gives the height in O(log n) time.
Binary Search:

The exists function determines if a node exists at a given index in the last level by performing a binary search. This check runs in O(log n) time.
The outer while loop in countNodes runs a binary search over the indices of the last level nodes, making the entire search O(log n * log n).
Total Nodes Calculation:

We calculate the total nodes by summing the nodes in all complete levels (which is 2^(ℎ𝑒𝑖𝑔ℎ𝑡−1) - 1 and the nodes in the last level (determined by binary search).
T
his approach ensures that the node count operation runs in 𝑂(log⁡𝑛 ⋅ log⁡𝑛), which is efficient for large complete binary trees.
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        # Calculate the height of the tree
        # Complete tree guarantees that only need to care about the left tree
        def get_height(node):
            height = 0
            while node:
                height += 1
                node = node.left
            return height
        
        height = get_height(root)
        
        if height == 1:
            return 1
        
        # Binary search to find the number of nodes in the last level
        def exists(index, height, node):
            left, right = 0, 2**(height - 1) - 1
            for _ in range(height - 1):
                mid = (left + right) // 2
                if index <= mid:
                    node = node.left
                    right = mid
                else:
                    node = node.right
                    left = mid + 1
            return node is not None
        
        left, right = 0, 2**(height - 1) - 1
        while left <= right:
            mid = (left + right) // 2
            if exists(mid, height, root):
                left = mid + 1
            else:
                right = mid - 1
        
        # Number of nodes in the complete levels + number of nodes in the last level
        return (2**(height - 1) - 1) + left

# Example Usage
root1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), None))
solution = Solution()
print(solution.countNodes(root1))  # Output: 6

root2 = None
print(solution.countNodes(root2))  # type: ignore # Output: 0

root3 = TreeNode(1)
print(solution.countNodes(root3))  # Output: 1
