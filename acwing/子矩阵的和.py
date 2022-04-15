# 前缀和
"""
输入一个 n 行 m 列的整数矩阵，再输入 q 个询问，每个询问包含四个整数 x1,y1,x2,y2，表示一个子矩阵的左上角坐标和右下角坐标。

对于每个询问输出子矩阵中所有数的和。

输入格式
第一行包含三个整数 n，m，q。

接下来 n 行，每行包含 m 个整数，表示整数矩阵。

接下来 q 行，每行包含四个整数 x1,y1,x2,y2，表示一组询问。

输出格式
共 q 行，每行输出一个询问的结果。

数据范围
1≤n,m≤1000,
1≤q≤200000,
1≤x1≤x2≤n,
1≤y1≤y2≤m,
−1000≤矩阵内元素的值≤1000
输入样例：
3 4 3
1 7 2 4
3 6 2 8
2 1 2 3
1 1 2 2
2 1 3 4
1 3 3 4
输出样例：
17
27
21
"""
""" 题解：
①构建前缀和二维数组。
parr[i][j] = parr[i-1][j] + parr[i][j-1] + arr[i][j] - p[i-1][j-1]
②利用前缀二维数组求区域和(x1, y1)(x2, y2)。
parr[x2][y2]-parr[x1-1][y2]-parr[x2][y1-1]+parr[x1-1][y1-1]

输入样例：
3 4 3
1 7 2 4
3 6 2 8
2 1 2 3
1 1 2 2
2 1 3 4
1 3 3 4
输出样例：
17
27
21
"""


def main():
    n, m, q = map(int, input().split())
    arr = [[0]*(m+1) for _ in range(n+1)]
    f = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        row = [0] + list(map(int, input().split()))
        for j in range(1, len(row)):
            arr[i][j] = row[j]

    for i in range(1, n+1):
        for j in range(1, m+1):
            f[i][j] = f[i-1][j] + f[i][j-1] - f[i-1][j-1] + arr[i][j]

    for i in range(q):
        x1, y1, x2, y2 = map(int, input().split())
        print(f[x2][y2]-f[x1-1][y2]-f[x2][y1-1]+f[x1-1][y1-1])


main()
