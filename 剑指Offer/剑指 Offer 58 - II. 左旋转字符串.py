"""
剑指 Offer 58 - II. 左旋转字符串
字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。



示例 1：

输入: s = "abcdefg", k = 2
输出: "cdefgab"
示例 2：

输入: s = "lrloseumgh", k = 6
输出: "umghlrlose"
"""
""" 题解
abcde k=2
=> edcba =>deabc
先全部翻转，然后前半部分和后半部分分别翻转。
"""


class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        n = n % len(s)
        s = list(s)
        def swap(s, i, j):
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        swap(s, 0, len(s)-1)
        swap(s, 0, len(s)-n-1)
        swap(s, len(s)-n, len(s)-1)
        return ''.join(s)


s = "abcdefg"
n = 2
solution = Solution()
print(solution.reverseLeftWords(s, n))
