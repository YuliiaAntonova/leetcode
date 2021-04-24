# You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

# Return the number of consistent strings in the array words.
# Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
# Output: 2
# Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.
class Solution:
    def countConsistentStrings(self, allowed, words):
        count=0
        for i in words:
            for j in i:
                if j not in allowed:
                    count +=1
                    break
        res=len(words)-count
        return res
if __name__ == '__main__':
    solution = Solution()
    print(solution.countConsistentStrings(allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]))
    print(solution.countConsistentStrings(allowed = "ab", words = ["ad","bd","aaab","baa","badab"]))
