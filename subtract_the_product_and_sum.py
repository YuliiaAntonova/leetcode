# Given an integer number n, return the difference between the product of its digits and the sum of its digits.
class Solution:
    def subtractProductAndSum(self,n):
        suma = 0                   #variable suma to assign 0
        mult = 1                   # variable mult to assign 1
        while n > 0:               # while the value of the variable> 0 repeat the following steps
            digit = n % 10         # find the remainder of dividing n by 10, that is, find the last digit

            suma = suma + digit    #add the extracted digit to the sum and increase the product by this digit
            mult = mult * digit
            n = n // 10
        return mult - suma

if __name__ == '__main__':
    solution = Solution()
    print(solution.subtractProductAndSum(234))
    print(solution.subtractProductAndSum(4421))





