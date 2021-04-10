# Given an array nums of integers, return how many of them contain an even number of digits.

class Solution:
    def findNumbers(self, nums):
        c = 0            # maintain counter
        for i in nums:
            j=str(i)     # from integer to string
            x = len(j)
            if x%2 == 0:
                c += 1   # return how many of them contain an even number of digits
        return c


if __name__ == '__main__':
    solution = Solution()
    print(solution.findNumbers([12,345,2,6,7896]))
    print(solution.findNumbers([555,901,482,1771]))
