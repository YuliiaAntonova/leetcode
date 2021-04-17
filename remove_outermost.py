class Solution:
    def removeOuterParentheses(self, S):
        # Stores the resultant string
        res = ""

        # Stores the count of
        # opened parentheses
        count = 0

        # Traverse the string
        for c in S:

            # If opening parenthesis is
            # encountered and their
            # count exceeds 0
            if (c == '(' and count > 0):
                # Include the character
                res += c

                # If closing parenthesis is
                # encountered and their
                # count is less than count
                # of opening parentheses
            if (c == '('):
                count += 1
            if (c == ')' and count > 1):
                # Include the character
                res += c

            if (c == ')'):
                count -= 1
        return res



if __name__ == '__main__':
    solution = Solution()
    print(solution.removeOuterParentheses("(()())(())(()(()))"))

