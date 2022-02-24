# Huffman树 贪心
""" Huffman树，又叫最优二叉树，是树的带权路径长度最小的二叉树。
节点的带权路径长度：从根节点到该节点的路径长度与该节点权的乘积。
树的带权路径长度：所有叶子节点的带权路径长度之和，记为WPL。
Huffman树应用了贪心思想，权值越小的节点离根节点越远，权值越大的节点离根节点越近。
若以词频为权，则高词频的词离根节点近（更容易遍历到），低词频的词离根节点越远（更不容易遍历）。
1 2 9
   12
   /\
  3 9
 /\
1 2
WPL=1*2+2*2+9*1=15
"""
from queue import PriorityQueue as PQ


def main():
    pq = PQ()
    n = int(input())
    arr = [int(i) for i in input().split()]
    for item in arr:
        pq.put(item)

    res = 0
    while pq.qsize() > 1:
        x = pq.get()
        y = pq.get()
        res += x + y
        pq.put(x + y)
    print(res)


main()
