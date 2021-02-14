# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".
class Solution:


    def longestCommonPrefix(self,strs) -> str:
        if not strs: return ""
        for i in range(len(strs[0])):      # the outer loop is for each character of the first word in the input array
            char = strs[0][i]
            for j in range(1, len(strs)):  # inner loop for each words
                if i == len(strs[j]) or strs[j][i] != char:
                    return strs[0][:i]
        return strs[0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestCommonPrefix(["flower", "flow", "flight"]))
    print(solution.longestCommonPrefix(["dog", "racecar", "car"]))
