# 区间和 离散化
"""
假定有一个无限长的数轴，数轴上每个坐标上的数都是 0。

现在，我们首先进行 n 次操作，每次操作将某一位置 x 上的数加 c。

接下来，进行 m 次询问，每个询问包含两个整数 l 和 r，你需要求出在区间 [l,r] 之间的所有数的和。

输入格式
第一行包含两个整数 n 和 m。

接下来 n 行，每行包含两个整数 x 和 c。

再接下来 m 行，每行包含两个整数 l 和 r。

输出格式
共 m 行，每行输出一个询问中所求的区间内数字和。

数据范围
−109≤x≤109,
1≤n,m≤105,
−109≤l≤r≤109,
−10000≤c≤10000
输入样例：
3 3
1 2
3 6
7 5
1 3
4 6
7 8
输出样例：
8
0
5
"""
""" 题解
稀疏数组范围特别大，无法使用前缀和解决，故考虑离散化。
①将原稀疏数组通过保序离散化方式将所有下标映射到一个稠密数组。
②求稠密数组LR下标所对应的区间和。
index_arr
1 3 4 6 7 8
arr
2 6 0 0 5 0 
prefix_arr
2 8 8 8 13 13

3 3
1 2
3 6
7 5
1 3
4 6
7 8
输出样例：
8
0
5
"""


def find(index_arr, index):
    """
    |_______||_____|
             o  (arr[mid]>=x，本质是求右区间边界点)
    """
    l, r = 0, len(index_arr)-1
    while l < r:
        mid = (l+r) // 2
        if index_arr[mid] >= index:
            r = mid
        else:
            l = mid+1
    # 因为后续要做前缀和操作，故映射后的索引要求从1开始
    return l+1


def main():
    N = 10**6
    m, q = map(int, input().split())
    index_arr = []
    add_list, query_list = [], []
    arr = [0] * N
    prefix_arr = [0] * N
    # index_arr存储所有索引
    for i in range(m):
        index, c = map(int, input().split())
        add_list.append((index, c))
        index_arr.append(index)
    for i in range(q):
        l, r = map(int, input().split())
        query_list.append((l, r))
        index_arr.append(l)
        index_arr.append(r)
    # 去重排序
    index_arr = sorted(list(set(index_arr)))
    # index_arr保存原数组所有索引(映射过程)，arr保存原数组所有的值（arr的索引与index_arr索引一致）。
    for i in range(m):
        index, c = add_list[i]
        idx = find(index_arr, index)
        arr[idx] += c

    # 构造前缀和数组
    for i in range(1, len(index_arr)+1):
        prefix_arr[i] = arr[i] + prefix_arr[i-1]

    # 利用前缀和数组求数组区间和
    for i in range(q):
        l, r = query_list[i]
        idx_l, idx_r = find(index_arr, l), find(index_arr, r)
        res = prefix_arr[idx_r] - prefix_arr[idx_l-1]
        print(res)


main()
