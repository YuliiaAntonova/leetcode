from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]):

        count = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                print(nums[count])
                nums[i], nums[count] = nums[count], nums[i]
                count += 1
        return (nums)


res = Solution()
result = res.moveZeroes([0, 1, 0, 3, 12])
print(result)


