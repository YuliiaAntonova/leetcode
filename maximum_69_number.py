# # Given a positive integer num consisting only of digits 6 and 9.
# #
# # Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).
# Input: num = 9669
# Output: 9969
# Explanation:
# Changing the first digit results in 6669.
# Changing the second digit results in 9969.
# Changing the third digit results in 9699.
# Changing the fourth digit results in 9666.
# The maximum number is 9969.

class Solution:
    def maximum69Number (self, num):
        n=str(num)
        list_n=list(n)                # convert num to string list
        for i in range(len(n)):
            if list_n[i]=="6":        # find “6” and replace it to “9" from high to low level
                list_n[i]="9"
                break
        s=''.join(list_n)
        return int(s)                  # convert string list to int
if __name__ == '__main__':
    a = Solution()

    print(a.maximum69Number(9669))


