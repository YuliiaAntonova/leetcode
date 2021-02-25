# Write a function that reverses a string. The input string is given as an array of characters char[].
#
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
#
# You may assume all the characters consist of printable ascii characters.

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return "".join(list(s)[::-1])
if __name__ == '__main__':
    a = Solution()
    print(a.reverseString(["h","e","l","l","o"]))
    print(a.reverseString(["H","a","n","n","a","h"]))