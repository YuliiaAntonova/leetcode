# Given an array of unique integers salary where salary[i] is the salary of the employee i.
#
# Return the average salary of employees excluding the minimum and maximum salary.
class Solution:
    def average(self,salary):
        salary.sort()
        s = salary[1:-1]
        sum = 0
        for i in s:
            sum += i
        return (sum / len(s))


if __name__ == '__main__':
    a = Solution()

    print(a.average([4000, 3000, 1000, 2000]))
