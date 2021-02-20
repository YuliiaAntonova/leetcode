class Solution:
    def numIdenticalPairs(self, nums):
        count = 0
        n=len(nums)

        for i in range(n):
            for j in range(n):
                if nums[i] == nums[j] and i > j:
                        count +=1
            j += 1
            i += 1


        return count



if __name__ == '__main__':
    solution = Solution()
    print(solution.numIdenticalPairs([1,2,3,1,1,3]))
    print(solution.numIdenticalPairs([1,1,1,1]))
    print(solution.numIdenticalPairs([1,2,3]))

