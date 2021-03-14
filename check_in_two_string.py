# Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.
# A string is represented by an array if the array elements concatenated in order forms the string.


class Solution:
    def arrayStringsAreEqual(self, word1, word2):
        f = "".join(word1); s = "".join(word2)        #Concatenate all strings in the first array into a single string in the given order, the same for the second array.
        return f == s

if __name__ == '__main__':
    a = Solution()

    print(a.arrayStringsAreEqual(["a", "cb"],["ab", "c"]))


