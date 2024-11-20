# You are given an integer array nums. In one operation, you can add or subtract 1 from any element of nums.
#
# Return the minimum number of operations to make all elements of nums divisible by 3.
#



from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operations = 0
        for num in nums:
            reminder = num%3
            if reminder == 1:
                operations +=1
            elif reminder == 2:
                operations +=1
        return operations