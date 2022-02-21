"""
第一种说法是 1 X Y，表示 X 和 Y 是同类。
第二种说法是 2 X Y，表示 X 吃 Y

当一句话满足下列三条之一时，这句话就是假话，否则就是真话。
当前的话与前面的某些真的话冲突，就是假话；
当前的话中 X 或 Y 比 N 大，就是假话；
当前的话表示 X 吃 X，就是假话。
输入样例：
100 7
1 101 1
2 1 2
2 2 3
2 3 3
1 1 3
2 3 1
1 5 5
输出样例：
3
"""

N = 50010
pre = [i for i in range(N)]
rank = [0 for i in range(N)]

def find(m):
    if m != pre[m]:
        pre[m] = find(pre[m])
    return pre[m]


def main():
    n, k = input().split()
    cnt = 0
    for _ in range(k):
        op, x, y = map(int, input().split())
        if x > n or y > n:
            cnt += 1
            continue
        if op == 1:
            pre[find(y)] = find(x)
        elif op == 2:
            if x == y:
                cnt += 1
                continue
            x_root, y_root = find(x), find(y)
            if rank[x_root] == 0 or rank[y_root] == 0:
                rank[x_root] = rank[y_root] + 1


