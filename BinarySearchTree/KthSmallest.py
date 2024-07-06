"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Example 1:
Input: root = [3,1,4,None,2], k = 1
Output: 1

Example 2:
Input: root = [5,3,6,2,4,None,None,1], k = 3
Output: 3
 

Constraints:

The number of nodes in the tree is n.
1 <= k <= n <= 10^4
0 <= Node.val <= 10^4
 

Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

If the BST is frequently modified (insertions and deletions), we can optimize the k-th smallest element retrieval by augmenting the BST nodes with additional information, such as the size of the subtree rooted at each node. This allows us to determine the rank of each node in O(logn) time during insertions, deletions, and searches.

Augmented Tree Node:
- Add an extra attribute size to each node to store the number of nodes in its subtree.
- Maintaining Size During Insertions and Deletions:
- Update the size attribute during each insertion and deletion operation.

Finding k-th Smallest:
- Use the size attribute to navigate the tree efficiently:
- Compare k with the size of the left subtree to decide whether to go left, right, or return the current node.
- This optimization ensures that both the tree operations (insert, delete) and the retrieval of the k-th smallest element run in O(logn) time, maintaining efficient performance even with frequent modifications.
"""

from TreeNode import TreeNode
from typing import Optional

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Initialize the stack for in-order traversal
        stack = []
        current = root
        count = 0
        
        while current or stack:
            # Go to the leftmost node
            while current:
                stack.append(current)
                current = current.left
            
            # Current must be None at this point
            current = stack.pop()
            count += 1
            
            # If count is equal to k, we've found our k-th smallest
            if count == k:
                return current.val
            
            # Otherwise, we move to the right subtree
            current = current.right
        return -1
    

s = Solution()

rarr = [3,1,4,None,2]
k = 1
root = TreeNode.generateTreeFromBFS(rarr)
print(s.kthSmallest(root, k))

rarr = [5,3,6,2,4,None,None,1]
k = 3
root = TreeNode.generateTreeFromBFS(rarr)
print(s.kthSmallest(root, k))
