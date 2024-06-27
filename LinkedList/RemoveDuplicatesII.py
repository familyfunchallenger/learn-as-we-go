"""
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.


Example 1:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:
Input: head = [1,1,1,2,3]
Output: [2,3]
 

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.

Solution should be straight forward:
- having a pointer traversing the list from the head towards the end of the list in a loop 
    * if current node's val is the same as the next node's val, remove next node
    * if current node's val is different form the next node's val, move the pointer downwards one node

"""