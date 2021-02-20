class Solution:
    def maximumWealth(self, x):
        y = []
        for i in range(len(x)):
            stroki = 0
            for j in range(len(x[i])):
                stroki += x[i][j]              # single line output
                y.append(stroki)               # with entry into a one-dimensional array
        return max(y)                          # return the maximum element of the new list


if __name__ == '__main__':
    solution = Solution()
    print(solution.maximumWealth([[1, 2, 3], [3, 2, 1]]))
    print(solution.maximumWealth([[1, 5], [7, 3], [3, 5]]))
    print(solution.maximumWealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]]))


