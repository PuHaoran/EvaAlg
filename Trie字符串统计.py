"""
维护一个字符串集合，支持两种操作：

I x 向集合中插入一个字符串 x；
Q x 询问一个字符串在集合中出现了多少次。
共有 N 个操作，输入的字符串总长度不超过 105，字符串仅包含小写英文字母。

输入格式
第一行包含整数 N，表示操作数。

接下来 N 行，每行包含一个操作指令，指令为 I x 或 Q x 中的一种。

输出格式
对于每个询问指令 Q x，都要输出一个整数作为结果，表示 x 在集合中出现的次数。

每个结果占一行。

数据范围
1≤N≤2∗104
输入样例：
5
I abc
Q abc
Q ab
I ab
Q ab
输出样例：
1
0
1
"""
""" 题解
Trie树，高效存储和查找字符串集合的数据结构，可以使用一个二维数组存储字典树结构，结尾地方存储字符串次数。
eg:
ab
abc
ac
bc
c
          -
        /   \  \
       a     b  c
      /\    /
     b- c-  c-
    /
   c-

5
I abc
Q abc
Q ab
I ab
Q ab
输出样例：
1
0
1
"""
idx = 0
N = 2 * 10**4
arr = [[0]*26 for _ in range(N)]
cnt = [0] * N


def insert(s):
    global idx
    p = 0
    for c in s:
        u = ord(c) - ord('a')
        if not arr[p][u]:
            idx += 1
            arr[p][u] = idx
        p = arr[p][u]
    cnt[p] += 1


def query(s):
    p = 0
    for c in s:
        u = ord(c) - ord('a')
        if not arr[p][u]:
            return 0
        p = arr[p][u]
    return cnt[p]


def main():
    n = int(input())
    for _ in range(n):
        op, s = input().split()
        if op == 'I':
            insert(s)
        elif op == 'Q':
            res = query(s)
            print(res)


main()
