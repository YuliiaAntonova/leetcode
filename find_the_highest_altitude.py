# Input: gain = [-5,1,5,0,-7]
# Output: 1
# Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.
class Solution:
    def largestAltitude(self, gain):
        res = [0]                          # created list res
        for i in range(len(gain)):
            res.append(res[i]+gain[i])      # add to new list item from list gain
        return max(res)                     # return a highest item

if __name__ == '__main__':
    a = Solution()

    print(a.largestAltitude([-5,1,5,0,-7]))


