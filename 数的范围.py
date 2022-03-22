# 二分
"""
给定一个按照升序排列的长度为 n 的整数数组，以及 q 个查询。

对于每个查询，返回一个元素 k 的起始位置和终止位置（位置从 0 开始计数）。

如果数组中不存在该元素，则返回 -1 -1。

输入格式
第一行包含整数 n 和 q，表示数组长度和询问个数。

第二行包含 n 个整数（均在 1∼10000 范围内），表示完整数组。

接下来 q 行，每行包含一个整数 k，表示一个询问元素。

输出格式
共 q 行，每行包含两个整数，表示所求元素的起始位置和终止位置。

如果数组中不存在该元素，则返回 -1 -1。

数据范围
1≤n≤100000
1≤q≤10000
1≤k≤10000
输入样例：
6 3
1 2 2 3 3 4
3
4
5
输出样例：
3 4
5 5
-1 -1
"""
""" 题解
整数二分，本质是找左区间的边界点或右区间的边界点。
①令x为边界点，写check(mid)函数满足覆盖左区间或右区间。
②缩小区间范围并递归。
l                    r
|_________||_________|
          oo <- 边界点
# 二分出左边界的边界点
mid = (l + r + 1) // 2
if check(mid):
    [mid, r] true
    [l, mid-1] false

# 二分出右边界的边界点
mid = (l + r) // 2
if check(mid):
    [l, mid] true
    [mid+1, r] false
eg:
6 3
1 2 2 3 3 4
3
4
5
令右边界的边界点为x=3，找满足条件的区间，arr[mid] >= x
|_________||_________|
           o 
1 2 2 3 3 4    (3) 
l         r
    mid
      l   r
        mid
      l r
      lr

"""

"""
二分出右区间边界点
|_________||_________|
           o 
1 2 2 3 3 4    (3) 
      o
"""


def bin_search1(arr, l, r, m):
    if l >= r:
        if m == arr[l]:
            return l
        else:
            return -1
    mid = (l + r) // 2
    if arr[mid] >= m:
        r = mid
    else:
        l = mid + 1
    return bin_search1(arr, l, r, m)


"""
二分出左区间边界点
|_________||_________|
          o
1 2 2 3 3 4    (3)
        o
"""


def bin_search2(arr, l, r, m):
    if l >= r:
        if m == arr[l]:
            return l
        else:
            return -1
    mid = (l + r + 1) // 2
    if arr[mid] <= m:
        l = mid
    else:
        r = mid-1
    return bin_search2(arr, l, r, m)


def main():
    n = [int(i) for i in input().split()][1]
    arr = [int(i) for i in input().split()]
    for i in range(n):
        m = int(input())
        res1 = bin_search1(arr, 0, len(arr)-1, m)
        res2 = bin_search2(arr, 0, len(arr)-1, m)
        print(res1, res2)


main()