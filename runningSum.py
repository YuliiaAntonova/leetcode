# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
#
# Return the running sum of nums.
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sums = []                                 # to create a new list
        sums.append(nums[0])                      # to  append index [0] from nums

        for i in range(1, len(nums)):             # to loop nums from nums[1]
            sum = sums[i-1] + nums[i]             # calculate the i-th number in the running sum from the (i-1)-th number
            sums.append(sum)                      # to append a new list

        return sums


s = Solution()
print(s.runningSum([1, 2, 3, 4]))
print(s.runningSum([1, 1, 1, 1, 1]))
print(s.runningSum([3, 1, 2, 10, 1]))