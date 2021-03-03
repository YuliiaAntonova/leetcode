class Solution:
    def fizzBuzz(self,n):
        res = []                                   # create a new list
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:          # if numbers are multiples of both three and five output “FizzBuzz”.
                res.append("FizzBuzz")
            elif i % 3 == 0:                       #  for multiples of three it should output “Fizz” instead of the number
                res.append("Fizz")
            elif i % 5 == 0:                       #  for the multiples of five output “Buzz”
                res.append("Buzz")
            else:
                res.append(str(i))
        return res


if __name__ == '__main__':
    a = Solution()
    print(a.fizzBuzz(15))
