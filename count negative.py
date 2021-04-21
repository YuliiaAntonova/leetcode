class Solution:
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        for i in grid:
            for j in i:
                if j < 0:
                    count += 1
        return count
if __name__ == '__main__':
    solution = Solution()
    print(solution.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))
