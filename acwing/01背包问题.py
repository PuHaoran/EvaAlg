"""
有 N 件物品和一个容量是 V 的背包。每件物品只能使用一次。

第 i 件物品的体积是 vi，价值是 wi。

求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。
输出最大价值。

输入格式
第一行两个整数，N，V，用空格隔开，分别表示物品数量和背包容积。

接下来有 N 行，每行两个整数 vi,wi，用空格隔开，分别表示第 i 件物品的体积和价值。

输出格式
输出一个整数，表示最大价值。

数据范围
0<N,V≤1000
0<vi,wi≤1000
输入样例
4 5
1 2
2 4
3 4
4 5
输出样例：
8
"""
""" 题解
DP问题
1) 状态表示。
    集合 满足条件的所有选法的集合。
        条件 ①只从前i个物品中选。②总体积<=j
    属性 max、min、数量
2) 状态计算(集合划分)。
    f(i, j) [不含i; 包含i]
            f(i-1, j) f(i-1, j-vi) + wi
=> 方程
f(i, j) = max(f(i-1, j), f(i-1, j-vi) + wi)
"""
"""
01背包
f(i,j)前i个物品<=j体积的最大价值。
f(i,j)=max(f(i-1,j), f(i-1, j-vi)+wi)

完全背包
f(i,j)前i个物品<=j体积的最大价值。
f(i,j)=max(f(i-1,j), f(i-1,j-vi)+wi, f(i-1,j-2vi)+2wi,...)            ①
f(i,j-vi)=max(f(i-1,j-vi), f(i-1,j-2vi)+wi, f(i-1,j-2vi)+2wi...)      ②
由①②得
f(i,j)=max(f(i-1,j), f(i,j-vi)+wi)

多重背包
f(i,j)前i个物品<=j体积的最大价值。
f(i,j)=max(f(i-1,j), f(i-1,j-vi)+wi...f(i-1,j-kvi)+kwi)

分组背包
f(i,j)前i组物品<=j体积的最大价值。
f(i,j)=max(f(i-1,j), f(i-1,j-vi)+wi)
"""


def main():
    N = 1010
    f = [[0] * N for i in range(N)]
    n, m = map(int, input().split())
    v, w = [0] * (n+1), [0] * (n+1)
    for i in range(1, n+1):
        _v, _w = map(int, input().split())
        v[i] = _v
        w[i] = _w

    for i in range(1, n+1):
        for j in range(1, m+1):
            f[i][j] = f[i-1][j]
            if j >= v[i]:
                f[i][j] = max(f[i][j], f[i-1][j-v[i]] + w[i])

    print(f[n][m])


main()
