"""
面试题50. 第一个只出现一次的字符
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

示例 1:

输入：s = "abaccdeff"
输出：'b'
示例 2:

输入：s = ""
输出：' '
"""


class Solution:
    def firstUniqChar(self, s: str) -> str:
        d = {}
        s = list(s)
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = 1
            else:
                d[s[i]] += 1
        for i in range(len(s)):
            if d[s[i]] == 1:
                return s[i]
        return ' '


s = "abaccdeff"
solution = Solution()
print(solution.firstUniqChar(s))