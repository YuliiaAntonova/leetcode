# // nums is passed in by reference. (i.e., without making a copy)
# int len = removeDuplicates(nums);
#
# // any modification to nums in your function would be known by the caller.
# // using the length returned by your function, it prints the first len elements.
# for (int i = 0; i < len; i++) {
#     print(nums[i]);
# }
class Solution:
    def removeDuplicates(self, nums):
        c = 0
        for i in nums:
            c += 1
            for j in range(c, len(nums)):
                if (i == nums[c]):
                    nums.remove(nums[c])
        return len(nums)


if __name__ == '__main__':
    a = Solution()

    print(a.removeDuplicates([1,1,2]))


