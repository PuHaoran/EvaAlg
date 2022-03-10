"""
剑指 Offer 59 - II. 队列的最大值
请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。

若队列为空，pop_front 和 max_value 需要返回 -1

示例 1：

输入:
["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
[[],[1],[2],[],[],[]]
输出: [null,null,null,2,1,2]
示例 2：

输入:
["MaxQueue","pop_front","max_value"]
[[],[],[]]
输出: [null,-1,-1]
"""
"""
一个队列用于存储原始数据，另外维持一个单调递增的双端队列。
"""


class MaxQueue:

    def __init__(self):
        self.p, self.q = -1, -1
        self.queue = [0] * 10010
        self.p2, self.q2 = -1, -1
        self.queue2 = [0] * 10010

    def max_value(self) -> int:
        if self.p2 == self.q2:
            return -1
        else:
            return self.queue2[self.p2+1]

    def push_back(self, value: int) -> None:
        self.q += 1
        self.queue[self.q] = value
        while self.p2 != self.q2 and value > self.queue2[self.q2]:
            self.q2 -= 1
        self.q2 += 1
        self.queue2[self.q2] = value

    def pop_front(self) -> int:
        if self.p == self.q:
            return -1
        t = self.queue[self.p+1]
        if t == self.queue2[self.p2+1]:
            self.p2 += 1
        self.p += 1
        return t
