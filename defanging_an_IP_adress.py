# string = "1.1.1.1"
# # Define your variables
# result = ''
# for i in string:
#         if i == ".":
#                 i = "[.]"
#         result += i
# print (result)
class Solution(object):
    def defangIPaddr(self, address):
        return address.replace(".", "[.]")
s = Solution()
print(s.defangIPaddr("1.1.1.1"))
print(s.defangIPaddr("255.100.50.0"))
