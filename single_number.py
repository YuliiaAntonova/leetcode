# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
#
# Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?

class Solution:
    def singleNumber(self, nums):
        for i in nums:
            if nums.count(i) == 1:      # a simple solusion, but count will iterate over the entire list each time
                return i

if __name__ == '__main__':
    a = Solution()
    print(a.singleNumber([2,2,1]))
    print(a.singleNumber([4,1,2,1,2]))
    print(a.singleNumber([1]))

# class Solution:
#     def singleNumber(self, nums):
#         res = 0
#         for i in nums:
#             res ^= i               # Operator sets each bit to 1 if only one of the bits is 1
#         return res



