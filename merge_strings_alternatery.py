# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
#
# Return the merged string.
class Solution:
    def mergeAlternately(self, word1, word2):
        p = min(len(word1), len(word2))
        m = max(len(word1), len(word2))

        w = ''
        for i in range(m):
            if i < len(word1):
                w += word1[i]

            if i < len(word2):
                w += word2[i]

        return (w)

if __name__ == '__main__':
    a = Solution()

    print(a.mergeAlternately("abc","pqr"))
    print(a.mergeAlternately("ab","pqrs"))



