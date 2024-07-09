"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

 

Example 1:


Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

Example 2:
Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.

Example 3:
Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.
 

Constraints:
* The number of nodes in the graph is in the range [0, 100].
* 1 <= Node.val <= 100
* Node.val is unique for each node.
* There are no repeated edges and no self-loops in the graph.
* The Graph is connected and all nodes can be visited starting from the given node.

Notes
Seems to be a DFS based solution with a mapping between the original nodes and the cloned nodes so that when a cloned node is referrenced after the initial creation, it can be retrieved from the mapping instead of be created again. 

With the two utility methods in Node.py, the clone is actually done - not the optimized solution though.
"""

from Node import Node
from typing import List, Optional



from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        new_node = None

        if not node:
            return new_node
        nodes = {}
        # two parses:
        # First one to populate the nodes mapping

        def dfs(node: Optional['Node']) -> None:
            if not node:
                return
            if node.val not in nodes:
                nodes[node.val] = Node(node.val)
            for n in node.neighbors:
                nodes[node.val].neighbors.append(n.val)
                if n.val not in nodes:
                    dfs(n)
        
        dfs(node)
        print(nodes)
        print(nodes[1].neighbors)
        print(nodes[2].neighbors)
        print(nodes[3].neighbors)
        print(nodes[4].neighbors)
        
        # for k, v in nodes.items():
        #     print('node: {0}; value as: {1}'.format(k, v))
        # populate neighbors by replacing the val with the actual nodes
        i = 0
        while i < len(nodes):
            neighbors = []
            print('i = ', i)
            print('nodes[i+1].neighbors - ', nodes[i + 1].neighbors)
            for j in nodes[i + 1].neighbors:
                print('j - in the neighbor population - ', j)
                neighbors.append(nodes[j])
            nodes[i + 1].neighbors = neighbors
            i += 1
        
        new_node = nodes[1]
        return new_node
    


s = Solution()

adjList = [[2,4],[1,3],[2,4],[1,3]]
node = Node.createGraphBasedOnAdjacenyList(adjList)
new_node = s.cloneGraph(node)
print(Node.convertGraphToList(new_node))