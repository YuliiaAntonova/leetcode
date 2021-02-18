# Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the ith kid has.
#
# For each kid check if there is a way to distribute extraCandies among the kids such that he or she can have the greatest number of candies among them.
# Notice that multiple kids can have the greatest number of candies.

class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        gretest=[]
        maxval=max(candies)
        for i in range(len(candies)):
            if candies[i] +extraCandies >= maxval:
                gretest.append(True)
            else:
                gretest.append(False)
        return gretest
s = Solution()
print(s.kidsWithCandies([2,3,5,1,3],3))
print(s.kidsWithCandies([4,2,1,1,2],1))
print(s.kidsWithCandies([12,1,12],10))
