"""
n−皇后问题是指将 n 个皇后放在 n×n 的国际象棋棋盘上，使得皇后不能相互攻击到，即任意两个皇后都不能处于同一行、同一列或同一斜线上。

1_597ec77c49-8-queens.png

现在给定整数 n，请你输出所有的满足条件的棋子摆法。

输入格式
共一行，包含整数 n。

输出格式
每个解决方案占 n 行，每行输出一个长度为 n 的字符串，用来表示完整的棋盘状态。

其中 . 表示某一个位置的方格状态为空，Q 表示某一个位置的方格上摆着皇后。

每个方案输出完成后，输出一个空行。

注意：行末不能有多余空格。

输出方案的顺序任意，只要不重复且没有遗漏即可。

数据范围
1≤n≤9
输入样例：
4
输出样例：
.Q..
...Q
Q...
..Q.

..Q.
Q...
...Q
.Q..
"""
""" 题解
剪枝：发现过滤条件，提前减少不必要的搜索路径。
定义列、正对角线、反对角线三个过滤条件数组，只有满足条件的才会继续深搜。
4
输出样例：
.Q..
...Q
Q...
..Q.

..Q.
Q...
...Q`
.Q..
"""


def dfs(u):
    if u == n:
        for i in range(n):
            print(''.join(path[i]))
        print()
        return
    for i in range(n):
        # 正对角线y=-x+b => x+y=b，反对角线y=x+b => b=y-x（b可能为负，故需要+n）
        if not col[i] and not dg[u+i] and not udg[i-u+n]:
            path[u][i], col[i], dg[u+i], udg[i-u+n] = 'Q', 1, 1, 1
            dfs(u+1)
            path[u][i], col[i], dg[u+i], udg[i-u+n] = '.', 0, 0, 0


def main():
    global n, path, row, col, dg, udg
    n = int(input())
    row, col, dg, udg = [0] * n, [0] * n, [0] * 2 * n, [0] * 2 * n
    path = [['.'] * n for _ in range(n)]
    u = 0
    dfs(u)


main()
