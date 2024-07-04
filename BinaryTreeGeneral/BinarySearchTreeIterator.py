"""
Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
int next() Moves the pointer to the right, then returns the number at the pointer.
Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.

 

Example 1:


Input
["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
Output
[null, 3, 7, true, 9, true, 15, true, 20, false]

Explanation
BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
bSTIterator.next();    // return 3
bSTIterator.next();    // return 7
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 9
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 15
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 20
bSTIterator.hasNext(); // return False
 

Constraints:

The number of nodes in the tree is in the range [1, 10^5].
0 <= Node.val <= 10^6
At most 105 calls will be made to hasNext, and next.
 

Follow up:

Could you implement next() and hasNext() to run in average O(1) time and use O(h) memory, where h is the height of the tree?

Feels like a stack based solution

"""

from TreeNode import TreeNode
from typing import Optional

class BSTIterator:

    # def __init__(self, root: Optional[TreeNode]):
    #     self.root = root
    #     self.stack = []
    #     self.traverse_visited = []
    #     self.next_visited = []
        # initialize the stack and the two visited sets
        # The stack has the nodes from the root to the left most leaf node in its left sub-tree, if the left sub-tree is none, the stack has the root itself. When it pops out the top of the stack, if the new top is already reported, pop out that one as well and push the right child of the popped out one on to the stack, if the new top has not been reported through the next() call, it will be returned by the subsequent next() invocation. If the top of the stack has an unvisited/unreported left child, need to push all the way through again to its current node's left most child in the left sub-tree.
        # The next_visited records all the nodes that have been returned by
        # next() calls
        # My above thoughts are aligned with GPT's suggestion

    def __init__(self, root: TreeNode):
        self.stack = []
        self._leftmost_inorder(root)
    
    def _leftmost_inorder(self, node):
        while node:
            self.stack.append(node)
            node = node.left
    
    def next(self) -> int:
        # Node at the top of the stack is the next smallest element
        topmost_node = self.stack.pop()
        
        # If the node has a right child, we push all the leftmost nodes starting from the right child
        if topmost_node.right:
            self._leftmost_inorder(topmost_node.right)
        
        return topmost_node.val
    
    def hasNext(self) -> bool:
        return len(self.stack) > 0
