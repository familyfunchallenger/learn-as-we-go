
from typing import List, Optional


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __str__(self) -> str:
        return '[val: {0}; neighbors: {1}]'.format(
            self.val,
            [n.val for n in self.neighbors]
        )

    @staticmethod
    def createGraphBasedOnAdjacenyList(
        adjList: List[List[int]]) -> Optional['Node']:
        """
        adjList is something like below:
        [[2,4],[1,3],[2,4],[1,3]] where each element list represents a node in the graph. The index is the same as the value of that node. and the element list itself represents the neighbors of the node.
        """
        if len(adjList) == 0:
            return None
        nodes = {}
        for i, n in enumerate(adjList):
            node = None
            if i not in nodes:
                node = Node(i + 1)
                nodes[i + 1] = node
            else:
                node = nodes[i + 1]
            if len(n) > 0:
                # need to create/populate neighbors
                for j in n:
                    if j not in nodes:
                        nodes[j] = Node(j)
                    node.neighbors.append(nodes[j])
            print(node)

        return nodes[1]


    @staticmethod
    def convertGraphToList(node: Optional['Node']) -> Optional[List[List[int]]]:
        if not Node:
            return None
        nodes = {}
        # two parses:
        # First one to populate the nodes mapping

        def dfs(node: Optional['Node']) -> None:
            if not node:
                return
            if node.val not in nodes:
                nodes[node.val] = node
            for n in node.neighbors:
                if n.val not in nodes:
                    dfs(n)
        
        dfs(node)
        print(nodes)
        ret = [[]]
        i = 0
        while i < len(nodes):
            neighbors = []
            for j in nodes[i + 1].neighbors:
                neighbors.append(j.val)
            ret.append(neighbors)
            i += 1
        ret.pop(0)
        return ret
    
# Test Below
#adjList = [[2,4],[1,3],[2,4],[1,3]]
#node = Node.createGraphBasedOnAdjacenyList(adjList)
# print(str(node))
# print(Node.convertGraphToList(node))