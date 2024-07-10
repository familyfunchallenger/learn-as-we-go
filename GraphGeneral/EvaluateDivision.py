"""
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

 

Example 1:
Input: 
equations = [["a","b"],["b","c"]] 
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
note: x is undefined => -1.0


Example 2:
Input: 
equations = [["a","b"],["b","c"],["bc","cd"]]
values = [1.5,2.5,5.0]
queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]


Example 3:
Input: 
equations = [["a","b"]]
values = [0.5]
queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]
 

Constraints:
* 1 <= equations.length <= 20
* equations[i].length == 2
* 1 <= Ai.length, Bi.length <= 5
* values.length == equations.length
* 0.0 < values[i] <= 20.0
* 1 <= queries.length <= 20
* queries[i].length == 2
* 1 <= Cj.length, Dj.length <= 5
* Ai, Bi, Cj, Dj consist of lower case English letters and digits.

"""

from typing import Dict, List, Optional
import math

class EquationNode:
    def __init__(
            self, name: str, 
            overs: Optional[Dict['EquationNode', float]] = None):
        self.name = name
        self.overs = overs if overs else {}

class Solution:
    def calcEquation(
            self, 
            equations: List[List[str]], 
            values: List[float],
            queries: List[List[str]]) -> List[float]:
        ret = []
        # ignore all the sanity checks for simplicity
        # establish a graph, may not be fully connected
        equation_nodes = {}
        for i, eq in enumerate(equations):
            if eq[0] not in equation_nodes:
                equation_nodes[eq[0]] = EquationNode(eq[0])
            if eq[1] not in equation_nodes:
                equation_nodes[eq[1]] = EquationNode(eq[1])
            equation_nodes[eq[0]].overs[equation_nodes[eq[1]]] = values[i]
            equation_nodes[eq[1]].overs[equation_nodes[eq[0]]] = 1 / values[i]

        def dfs(start_node_str: str, end_node_str: str) -> float:
            # Use DFS to find if there is a path from start_node to end_node.
            # If so, calculate the return value by the productions of the all 
            # the x over y values along the path. If there is no path from 
            # the given start_node to the end_node in the equation_nodes,
            # return -1.0
            print('start and end: ', start_node_str, end_node_str)
            if (start_node_str not in equation_nodes 
                or end_node_str not in equation_nodes):
                return -1.0
            if (start_node_str == end_node_str):
                return 1.0
            start_node = equation_nodes[start_node_str]
            end_node = equation_nodes[end_node_str]
            visited.append(start_node)
            for n in start_node.overs:
                if n in visited:
                    continue
                visited.append(n)
                r = dfs(n.name, end_node.name)
                if not math.isclose(r, -1.0):
                    return start_node.overs[n] * r
            return -1.0
        
        for q in queries:
            visited = []
            ret.append(dfs(q[0], q[1])) # type: ignore
            
        return ret


s = Solution()

equations = [["a","b"],["b","c"]] 
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
ret = s.calcEquation(equations, values, queries)
print(ret)
