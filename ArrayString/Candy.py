"""
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

 

Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.


Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
 

Constraints:

n == ratings.length
1 <= n <= 2 * 104
0 <= ratings[i] <= 2 * 104
"""


from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        i = 0
        total_candies = 0
        while i < len(ratings) - 1:
            # only check on the len(ratings) - 1 items
            # the last one will be handled as a special case
            # after all other items are settled.
            going_up_items = 0
            going_down_items = 0
            base_candy = 1
            last_candy = 1
            previous_trend = 0  # 1 going up, -1 going down, 0 flat
            if ratings[i] < ratings[i + 1]:
                # start of an UP trend
                going_up_items = 0
                while ratings[i] < ratings[i + 1]:
                    if previous_trend == 0:
                        # flat before this, candy has to start from the candy
                        # given to ratings[i]
                        if i == 0:
                            base_candy = 1
                        else:
                            base_candy = last_candy
                    elif previous_trend == -1:
                        # down trend before, base candy has to be 1
                        base_candy = 1
                    total_candies += going_up_items + base_candy
                    going_up_items += 1
                    i += 1
                # when we get out of the loop here, we are at the last item
                # of the up trend, but this item is not counted
                total_candies += going_up_items + base_candy
                i += 1
                last_candy = going_up_items + base_candy
                previous_trend = 1
            if ratings[i] == ratings[i + 1]:
                # start of a FLAT trend
                if previous_trend == -1:
                    # it was DOWN trend before, so the base candy and last candy should be 1
                    base_candy = 1
                    last_candy = 1
                elif previous_trend == 1:
                    # it was UP trend before, so the base candy is the last candy at the end of UP trend
                    base_candy = last_candy
                while ratings[i] == ratings[i + 1]:
                    total_candies += base_candy
                    i += 1
                # when we get out of the loop, the last item in the FLAT trend has not been processed
                total_candies += base_candy
                i += 1
                previous_trend = 0
            if ratings[i] > ratings[i + 1]:
                # start of a DOWN trend
                # the last element of the ratings[i] will get 1 candy
                # thus the base_candy will start from 1 and the last candy here will be 1 as well
                going_down_items = 0
                while ratings[i] > ratings[i + 1]:
                    total_candies += going_down_items + 1
                    going_down_items += 1
                    i += 1
                # after getting out of the loop above, the rating[i + 1] is not processed
                total_candies += going_down_items + 1
                last_candy = 1
                previous_trend = -1
        # now we are out of the entire loop and need to handle ratings[-1]
        if ratings[-1] == ratings[-2]:
            total_candies += last_candy
        elif ratings[-1] < ratings[-2]:
            total_candies += 1
        else:
            total_candies += last_candy + 1
        return total_candies