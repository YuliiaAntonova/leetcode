# Given a non-negative integer. Return the number of steps to reduce it to zero.
# If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.
class Solution:
    def numberOfSteps(self, nums):
        count=0
        while nums != 0:                    # while nums is not equal to 0
            if nums%2==0:                   # if nums is even
                nums = nums//2              # reassign nums to be nums divided by 2
            else:                           # nums is odd
                nums = nums - 1             # reassign nums to be nums minus 1
            count += 1
        return count

if __name__ == '__main__':
    a = Solution()
    print(a.numberOfSteps(123))
    print(a.numberOfSteps(0))
