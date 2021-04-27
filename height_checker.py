class Solution:
    def heightChecker(self, heights):
        sorted_list = sorted(heights)
        count=0
        for i in range(len(heights)):
            if heights[i] != sorted_list[i]:
                count += 1
        return count

if __name__ == '__main__':
    solution = Solution()
    print(solution.heightChecker([1,1,4,2,1,3]))
    print(solution.heightChecker([5,1,2,3,4]))
    print(solution.heightChecker([1,2,3,4,5]))

