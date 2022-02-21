"""
输入一个长度为 n 的整数数列，从小到大输出前 m 小的数。

输入格式
第一行包含整数 n 和 m。

第二行包含 n 个整数，表示整数数列。

输出格式
共一行，包含 m 个整数，表示整数数列中前 m 小的数。

数据范围
1≤m≤n≤105，
1≤数列中元素≤109
输入样例：
5 3
4 5 1 3 2
输出样例：
1 2 3
"""
""" 题解
堆的存储
  1
 / \
2x 2x+1
堆的基本操作down和up
       6
     /  \
    3   4
   /\   /\
  3 5  4 5
=>
       3
     /  \
    6   4
   /\   /\
  3 5  4 5
=>
       3
     /  \
    3   4
   /\   /\
  6 5  4 5
手写堆
1. 插入一个数
heap[++size]=x
up(size)
2. 求堆的最小值
heap[1]
3. 删除最小值
heap[1]=heap[size]
size--
down(1)
4. 删除任意一个元素
heap[k]=heap[size]
size--
down(k)
up(k)
5. 修改任意一个元素
heap[k]=x
down(k)
up(k)
5 3
4 5 1 3 2
输出样例：
1 2 3

为何建堆时从n//2开始？
假设堆共有5个元素，则数组对应索引为
        1
       /\
      2 3
     /\
    4 5
5//2=2是除叶子节点最大的元素，而叶子节点是不需要进行down的；
从后向前遍历可以保证当前情况满足条件之后后续的节点都是比当前节点大的，无需继续down。
"""


def down(i):
    t = i
    if i * 2 <= n and h[i * 2] < h[t]:
        t = i * 2
    if i * 2 + 1 <= n and h[i * 2 + 1] < h[t]:
        t = i * 2 + 1
    if t != i:
        h[i], h[t] = h[t], h[i]
        down(t)


def main():
    global h, n
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    h = [0] + arr

    # 建堆
    for i in range(n//2, 0, -1):
        down(i)
    # 删除最小值
    for i in range(m):
        print(h[1], end=' ')
        h[n], h[1] = h[1], h[n]
        n -= 1
        down(1)


main()
