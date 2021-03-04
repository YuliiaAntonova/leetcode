# Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

# Given a balanced string s, split it in the maximum amount of balanced strings.

# Return the maximum amount of split balanced strings.
# Runtime: 28 ms, faster than 85.36% of Python3 online submissions for Split a String in Balanced Strings.
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l = 0
        r = 0
        count = 0
        for i in s:
            if i == 'L':  # Loop from left to right maintaining a balance variable when it gets an L increase it by one otherwise decrease it by one.
                l += 1
            else:
                r += 1
            if l == r:
                count += 1

        return count


s = Solution()
ss = "RLLLLRRRLR"
# "LLLLRRRR"
print(s.balancedStringSplit(ss))