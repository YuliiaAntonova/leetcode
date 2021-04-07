# Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
#
# You may return any answer array that satisfies this conditio

class Solution:
    def sortArrayByParity(self, A):
        res=[]     # create a new list
        a=[]
        for i in A:
            if i%2==0:
                res.append(i)    # add a even items in new list
            else:
                a.append(i)      # else odd items in other list
        return res+a
if __name__ == '__main__':
    solution = Solution()
    print(solution.sortArrayByParity([3,1,2,4]))
