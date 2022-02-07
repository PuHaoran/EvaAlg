# 归并排序
"""
给定一个长度为 n 的整数数列，请你计算数列中的逆序对的数量。

逆序对的定义如下：对于数列的第 i 个和第 j 个元素，如果满足 i<j 且 a[i]>a[j]，则其为一个逆序对；否则不是。

输入格式
第一行包含整数 n，表示数列的长度。

第二行包含 n 个整数，表示整个数列。

输出格式
输出一个整数，表示逆序对的个数。

数据范围
1≤n≤100000，
数列中的元素的取值范围 [1,109]。

输入样例：
6
2 3 4 5 6 1
输出样例：
5
"""
""" 题解
1）中间元素作为分界点，划分Left和Right区间。此时，逆序对包括3种，全在左区间，全在右区间，左右区间各一个。
2）递归左右区间。
3）归并排序进行双指针算法时，若i对应元素>j对应元素，则i之后的元素都大于j对应元素。此时表示j有mid-i+1个逆序对。
2 3 4 5 6 1

2 3 4   1 5 6
i       j     (3)
    i       j
5 6   1
i     j   (2)

"""
temp = [0] * 100010


def merge_sort(arr, l, r):
    if l >= r:
        return 0
    mid = (l + r) >> 1
    res = merge_sort(arr, l, mid) + merge_sort(arr, mid+1, r)
    i, j, k = l, mid+1, 0
    while i <= mid and j <= r:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            res += mid-i+1
            temp[k] = arr[j]
            j += 1
        k += 1
    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1
    while j <= r:
        temp[k] = arr[j]
        j += 1
        k += 1
    for i in range(k):
        arr[l+i] = temp[i]
    return res


def main():
    n = input()
    arr = [int(i) for i in input().split()]
    res = merge_sort(arr, 0, len(arr)-1)
    print(res)


main()
