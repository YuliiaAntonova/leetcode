# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.

class Solution(object):
    def twoSum(self, arr, target) -> object:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(arr)
        for i in range(0, n):
            for j in range(i + 1, n):
                if (arr[i] + arr[j])  == target:
                    return [i,j]

if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum([2,7,11,5],9))
    print(solution.twoSum([0, 4, 3, 0],0))

