# Given a string s and an integer array indices of the same length.
#
# The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.
#
# Return the shuffled string.
class Solution:
    def restoreString(self, s: str, indices):
        res = ['']*len(s)
        for index,char in enumerate(s):
            res[indices[index]] = char
        return ''.join(res)
if __name__ == '__main__':
    a = Solution()

    print(a.restoreString("codeleet",[4,5,6,7,0,2,1,3]))


# class Solution:
#     def restoreString(self, s, indices):
#         list1, list2 = zip(*sorted(zip(indices, s)))
#         ans = ''
#         for i in range(len(s)):
#             ans += list2[i]
#         return ans