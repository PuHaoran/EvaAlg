# 排序
"""
给定你一个长度为 n 的整数数列。

请你使用归并排序对这个数列按照从小到大进行排序。

并将排好序的数列按顺序输出。

输入格式
输入共两行，第一行包含整数 n。

第二行包含 n 个整数（所有整数均在 1∼109 范围内），表示整个数列。

输出格式
输出共一行，包含 n 个整数，表示排好序的数列。

数据范围
1≤n≤100000
输入样例：
5
3 1 2 4 5
输出样例：
1 2 3 4 5
"""
""" 题解
归并排序
1）确定一个分界点l+r // 2。
2）递归Left和Right。
3）归并-合二为一，通过临时数组存储排序后的数据，然后赋值给原数组。

3 1 2 4 5
3 1 2   4 5
3 1   2    4   5
3   1   2   4   5
1 3 => 1 2 3
4 5
=> 1 2 3 4 5
"""

temp = [0] * 100010
def merge_sort(arr, l, r):
    if l >= r:
        return
    mid = (l + r) >> 1
    merge_sort(arr, l, mid)
    merge_sort(arr, mid+1, r)
    i, j, k = l, mid+1, 0
    while i <= mid and j <= r:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
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

    for i in range(0, r-l+1):
        arr[l+i] = temp[i]


def main():
    n = input()
    arr = [int(i) for i in input().split()]
    merge_sort(arr, 0, len(arr)-1)
    for i in arr:
        print(i, end=' ')


main()
