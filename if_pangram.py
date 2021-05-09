# A pangram is a sentence where every letter of the English alphabet appears at least once.

# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

class Solution:
    def checkIfPangram(self, sentence):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for i in alphabet:
            if i not in sentence.lower():
                return False
        return True

if __name__ == '__main__':
    a = Solution()

    print(a.checkIfPangram(sentence = "thequickbrownfoxjumpsoverthelazydog"))
    print(a.checkIfPangram(sentence="leetcode"))
