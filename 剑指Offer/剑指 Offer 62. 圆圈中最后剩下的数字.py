"""
剑指 Offer 62. 圆圈中最后剩下的数字
0,1,···,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字（删除后从下一个数字开始计数）。求出这个圆圈里剩下的最后一个数字。

例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。



示例 1：

输入: n = 5, m = 3
输出: 3
示例 2：

输入: n = 10, m = 17
输出: 2
"""
""" 题解
             0
          n-1   1
          6     m-1 (去掉m-1，m-1之后重新进行编号)
          5     m 0
            4 
            1
            
f(n, m)表示最后还剩一个元素的位置，当去掉一个元素时，从去掉元素的下一个位置重新编号，相当于f(n-1,m)，而从图中可以发现f(n-1,m)和f(n,m)所有编号间存在如下映射关系。
f(n,m)=(f(n-1,m)+m) % n，且f(1,m)=0。
"""


class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        res = 0
        for i in range(2, n+1):
            res = (res+m) % i
        return res
