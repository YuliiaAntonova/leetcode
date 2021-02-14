class Solution(object):
    def isPalindrome(self,n):
        """This function checks to see if the given entry is palindrome or not"""

        # The original entry (A number or a word)
        Original = str(n)

        # Reversing the entry
        Reverse = Original[::-1]

        # Checking to see if the two are equal
        if Original == Reverse:
            return True
        else:
            return False
if __name__ == '__main__':

    solution = Solution()
    print(solution.isPalindrome(121))
    print(solution.isPalindrome(1234))



