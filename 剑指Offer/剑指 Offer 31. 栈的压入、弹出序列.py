"""
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如，序列 {1,2,3,4,5} 是某栈的压栈序列，序列 {4,5,3,2,1} 是该压栈序列对应的一个弹出序列，但 {4,3,5,1,2} 就不可能是该压栈序列的弹出序列。

示例 1：

输入：pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
输出：true
解释：我们可以按以下顺序执行：
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
示例 2：

输入：pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
输出：false
解释：1 不能在 2 之前弹出。
"""
""" 题解
定义一个栈，遍历pushed，直接对元素入栈，若当前栈顶元素等于出栈数组元素，则弹出并出栈数组进一。
"""

class Solution:
    def validateStackSequences(self, pushed, popped):
        j = 0
        top = -1
        s = [0]*1010
        for i in range(len(pushed)):
            top += 1
            s[top] = pushed[i]
            while top != -1 and s[top] == popped[j]:
                top -= 1
                j += 1
        if top == -1 and j == len(popped):
            return True
        return False


pushed = [1,2,3,4,5]
popped = [4,3,5,1,2]
solution = Solution()
print(solution.validateStackSequences(pushed, popped))

