from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]):

        def get_key(log):
            identifier, content = log.split(" ", 1)

            return (0, content, identifier) if content[0].isalpha() else (1, )

        return sorted(logs, key=get_key)


res = Solution()
result = res.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"])
print(result)

