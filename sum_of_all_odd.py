# Given an array of positive integers arr, calculate the sum of all possible odd-length subarrays.
# A subarray is a contiguous subsequence of the array.
# Return the sum of all odd-length subarrays of arr.

class Solution:
    def sumOddLengthSubarrays(self, arr):
        res = 0
        for i in range(len(arr)):
            for j in range(i,len(arr),2):
                s = sum(arr[i:j + 1])
                res += s
        return res

if __name__ == '__main__':
    a = Solution()

    print(a.sumOddLengthSubarrays([1,4,2,5,3]))








