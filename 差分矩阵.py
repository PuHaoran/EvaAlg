# 差分矩阵
"""
输入一个 n 行 m 列的整数矩阵，再输入 q 个操作，每个操作包含五个整数 x1,y1,x2,y2,c，其中 (x1,y1) 和 (x2,y2) 表示一个子矩阵的左上角坐标和右下角坐标。

每个操作都要将选中的子矩阵中的每个元素的值加上 c。

请你将进行完所有操作后的矩阵输出。

输入格式
第一行包含整数 n,m,q。

接下来 n 行，每行包含 m 个整数，表示整数矩阵。

接下来 q 行，每行包含 5 个整数 x1,y1,x2,y2,c，表示一个操作。

输出格式
共 n 行，每行 m 个整数，表示所有操作进行完毕后的最终矩阵。

数据范围
1≤n,m≤1000,
1≤q≤100000,
1≤x1≤x2≤n,
1≤y1≤y2≤m,
−1000≤c≤1000,
−1000≤矩阵内元素的值≤1000
输入样例：
3 4 3
1 2 2 1
3 2 2 1
1 1 1 1
1 1 2 2 1
1 3 2 3 2
3 1 3 4 1
输出样例：
2 3 4 1
4 3 4 1
2 2 2 2
"""
""" 题解
①根据原矩阵求差分矩阵
diff_arr[i][j] = arr[i][j] + arr[i-1][j-1] - arr[i-1][j] - arr[i][j-1]
②基于差分矩阵前面的元素+c，后面原矩阵所有元素均+c的性质进行原矩阵区域+c。
3 4 3
1 2 2 1
3 2 2 1
1 1 1 1
1 1 2 2 1
1 3 2 3 2
3 1 3 4 1

2 3 4 1
4 3 4 1
2 2 2 2
"""


def main():
    N = 1010
    arr = [[0]*N for _ in range(N)]
    diff_arr = [[0]*N for _ in range(N)]
    res = [[0]*N for _ in range(N)]
    m, n, q = map(int, input().split())
    for i in range(m):
        rows = list(map(int, input().split()))
        for j in range(len(rows)):
            arr[i+1][j+1] = rows[j]

    # 差分矩阵
    for i in range(1, m+1):
        for j in range(1, n+1):
            diff_arr[i][j] = arr[i][j] + arr[i-1][j-1] - arr[i-1][j] - arr[i][j-1]

    for i in range(q):
        x1, y1, x2, y2, c = map(int, input().split())
        diff_arr[x1][y1] += c
        diff_arr[x1][y2+1] -= c
        diff_arr[x2+1][y1] -= c
        diff_arr[x2+1][y2+1] += c

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            res[i][j] = res[i-1][j] + res[i][j-1] + diff_arr[i][j] - res[i-1][j-1]

        print(' '.join(list(map(str, res[i][1:n+1]))))


main()
