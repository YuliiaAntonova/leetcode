# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it.
# That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

# Return the answer in an array.
class Solution:
    def smallerNumbersThanCurrent(self, nums):
        result = []
        for i in nums:              #  for each number i
            count = 0
            for j in nums:          # run a comparison number looping
                if i > j:           # if the number is greater than the comparison number, increment the counter
                    count += 1
            result.append(count)

        return result



if __name__ == '__main__':
    solution = Solution()
    print(solution.smallerNumbersThanCurrent([8,1,2,2,3]))
    print(solution.smallerNumbersThanCurrent([6,5,4,8]))
    print(solution.smallerNumbersThanCurrent([7,7,7,7]))


