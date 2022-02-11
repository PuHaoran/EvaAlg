"""
实现一个单链表，链表初始为空，支持三种操作：

向链表头插入一个数；
删除第 k 个插入的数后面的数；
在第 k 个插入的数后插入一个数。
现在要对该链表进行 M 次操作，进行完所有操作后，从头到尾输出整个链表。

注意:题目中第 k 个插入的数并不是指当前链表的第 k 个数。例如操作过程中一共插入了 n 个数，则按照插入的时间顺序，这 n 个数依次为：第 1 个插入的数，第 2 个插入的数，…第 n 个插入的数。

输入格式
第一行包含整数 M，表示操作次数。

接下来 M 行，每行包含一个操作命令，操作命令可能为以下几种：

H x，表示向链表头插入一个数 x。
D k，表示删除第 k 个插入的数后面的数（当 k 为 0 时，表示删除头结点）。
I k x，表示在第 k 个插入的数后面插入一个数 x（此操作中 k 均大于 0）。
输出格式
共一行，将整个链表从头到尾输出。

数据范围
1≤M≤100000
所有操作保证合法。

输入样例：
10
H 9
I 1 1
D 1
D 0
H 6
I 3 6
I 4 5
I 4 5
I 3 4
D 6
输出样例：
6 4 6 5
"""
""" 题解
e[N] 保存值
ne[N] 保存next指针
      3  5  7  9
      o->o->o->o->...
      0  1  2  3  -1
head=0
e[0]=3  e[1]=5  e[2]=7  e[3]=9
ne[0]=1 ne[1]=2 ne[2]=3 ne[3]=-1
参考链接
https://www.acwing.com/solution/content/39929/
"""
N = 100010
e, ne = [0] * N, [0] * N
head, idx = -1, 0


def add_head(x):
    """ 插入一个头节点 """
    global idx
    global head
    e[idx] = x
    ne[idx] = head
    head = idx
    idx += 1


def add(k, x):
    """ k索引后插入一个节点x """
    global idx
    e[idx] = x
    ne[idx] = ne[k]  # 新节点插入到k节点之后
    ne[k] = idx
    idx += 1


def remove(k):
    """ k索引后删除一个节点 """
    ne[k] = ne[ne[k]]


def main():
    global head
    n = int(input())
    for _ in range(n):
        row = input().split()
        if row[0] == 'H':
            add_head(int(row[1]))
        elif row[0] == 'I':
            k, x = int(row[1])-1, int(row[2])
            add(k, x)
        elif row[0] == 'D':
            if row[1] == '0':
                head = ne[head]
            else:
                k = int(row[1])-1
                remove(k)
    i = head
    while i != -1:
        print(e[i], end=' ')
        i = ne[i]


main()
