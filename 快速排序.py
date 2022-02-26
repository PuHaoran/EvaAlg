# 排序
"""
给定你一个长度为 n 的整数数列。

请你使用快速排序对这个数列按照从小到大进行排序。

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
 3 1 2 4 5
i         j
 i   j
 2 1 3 4 5
   j i 
 2 1      3 4 5
i   j    i     j 
 i j      ij    
 1 2      3   4 5
 j i          4   5
 1   2  
|______|  |___|
       j  j+1
      <=x >x      
两指针从左右两端向中间靠拢，i和j要求满足arr[i] < x, arr[j] < x，若不满足且i < j则交换两者位置；
当i >= j时，此时可将区间分位[l, j], [j+1, r](arr[j] <= x, arr[j+1] >= x)。

论证i和j一定不会过界。
1. |_________________|
   ij
情况一，i和j都在首位置，因为不满足i<j，则直接进行下次函数递归，不用担心过界。
2. |a            b|
   |______________x__|
   i              j
情况二，i在首位置，j在其他位置，则交换i和j此时对于j而言a位置就是边界，对于i而言b位置就是边界，故也不用担心过界。
"""


def quick_sort(l, r):
    if l >= r:
        return
    x = arr[(l+r)//2]
    i, j = l-1, r+1
    while i < j:
        while 1:
            i += 1
            if arr[i] >= x:
                break
        while 1:
            j -= 1
            if arr[j] <= x:
                break
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    quick_sort(l, j)
    quick_sort(j+1, r)


def main():
    global arr
    n = int(input())
    arr = list(map(int, input().split()))
    quick_sort(0, len(arr)-1)
    print(' '.join([str(i) for i in arr]))


main()
