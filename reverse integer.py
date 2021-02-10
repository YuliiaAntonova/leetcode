# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
class Solution(object):

    def reverse(self,n):
        y = str(abs(n)) # Create a variable and convert the integer into a string
        y = y.strip()   #Strip all the leading zeros
        y = y[::-1]     #reversed str
        rev = int(y)    #Input reverse as an integer
        if rev >= 2 **31 -1 or rev <= -2**31: #check the conditions
            return 0
        elif n < 0:     #display negative numbers
            return -1 * rev
        else:
            return rev
if __name__ == '__main__':

    solution = Solution()
    print(solution.reverse(-123))
    print(solution.reverse(1234))


