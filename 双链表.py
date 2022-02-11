""" 题解
10
R 7
D 1
L 3
IL 2 10
D 3
IL 2 7
L 8
R 9
IL 4 7
IR 2 2
输出样例：
8 7 7 3 2 9
"""
# 初始化左右节点
N = 1010
e, r, l = [0] * N, [0] * N, [0] * N
r[0], l[1] = 1, 0
idx = 2


def add(k, x):
    """ 索引为k的数后添加x """
    global idx
    e[idx] = x
    l[idx] = k
    r[idx] = r[k]
    l[r[idx]] = idx
    l[idx] = k
    idx += 1


def remove(k):
    """ 删除索引为k的点 """
    l[r[k]] = l[k]
    r[l[k]] = r[k]


def main():
    n = int(input())
    for _ in range(n):
        row = input().split()
        if row[0] == 'R':
            x = int(row[1])
            add(0, x)
        elif row[0] == 'L':
            x = int(row[1])
        elif row[0] == 'D':
            k = int(row[1])
        elif row[0] == 'IL':
            pass
        elif row[0] == 'IR':
            pass


main()
