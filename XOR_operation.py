# Given an integer n and an integer
# Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length
# Return the bitwise XOR of all elements of nums
class Solution:
    def xorOperation(self, n, start):
        value = 0
        for x in range(n):
            value = (start + 2 * x)

        return value
if __name__ == '__main__':
    a = Solution()

    print(a.xorOperation(5,0))


