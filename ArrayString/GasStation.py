"""
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station.
 You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction,
 otherwise return -1. If there exists a solution, it is guaranteed to be unique

 

Example 1:

Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.


Example 2:

Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.
 

Constraints:

n == gas.length == cost.length
1 <= n <= 105
0 <= gas[i], cost[i] <= 104
"""


from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start_position = 0
        length = len(gas)
        while start_position < length:
            if gas[start_position] < cost[start_position]:
                # At this starting position, if current available gas is not enough to move to next gas station, we cannot choose this one as the starting
                # point
                start_position += 1
                continue
            steps = 0
            i = start_position
            avail_gas = gas[start_position]
            while steps < length:
                avail_gas = avail_gas - cost[i] + gas[(i + 1) % length]
                if avail_gas < cost[(i + 1) % length]:
                    # cannot move further after this move
                    break
                steps += 1
                i = ( i + 1) % length
            if steps == length:
                # finished one whole trip to all gas stations
                return start_position
            else:
                # got out above loop without finishing all gas stations, try next start position
                start_position += 1
        return -1
    

s = Solution()

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
print(s.canCompleteCircuit(gas, cost))

gas = [2,3,4]
cost = [3,4,3]
print(s.canCompleteCircuit(gas, cost))