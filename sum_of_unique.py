# You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.
#
# Return the sum of all the unique elements of nums.

class Solution:
    def sumOfUnique(self, nums):
        s = 0
        for num in nums:
            if nums.count(num) == 1:
                s += num
        return s
if __name__ == '__main__':

    solution = Solution()
    print(solution.sumOfUnique([1,1,1,1,1]))
    print(solution.sumOfUnique([1,2,3,2]))
    print(solution.sumOfUnique([1,2,3,4,5]))