# Given a sentence that consists of some words separated by a single space, and a searchWord.
#
# You have to check if searchWord is a prefix of any word in sentence.
#
# Return the index of the word in sentence where searchWord is a prefix of this word (1-indexed).
#
# If searchWord is a prefix of more than one word, return the index of the first word (minimum index). If there is no such word return -1.
#
# A prefix of a string S is any leading contiguous substring of S.
class Solution:
  def isPrefixOfWord(self, sentence, searchWord):
    sentence = sentence.split(' ')
    for index,word in enumerate(sentence):
        if searchWord == word[:len(searchWord)]:
            return index+1
    return -1

if __name__ == '__main__':
    a = Solution()

    print(a.isPrefixOfWord("i love eating burger","burg"))
    print(a.isPrefixOfWord("this problem is an easy problem","pro"))