""" 题解
双指针算法核心思想是运用某些性质将O(n^2)优化为O(n)。
5
1 2 2 3 5

1 2 2 3 5
j   i
    ji
    j   i
"""


def get_longest(arr):
    """ 双指针做法 """
    res, j = 0, 0
    s = [0] * 100010
    for i in range(len(arr)):
        s[arr[i]] += 1
        while s[arr[i]] > 1 and j <= i:
            s[arr[j]] -= 1
            j += 1
        if i-j+1 > res:
            res = i-j+1
    return res


# def get_longest(arr):
#     """ 暴力做法 """
#     res = 0
#     for i in range(len(arr)):
#         s = [0] * 100010
#         cnt = 0
#         for j in range(i, len(arr)):
#             if s[arr[j]] > 0:
#                 break
#             else:
#                 s[arr[j]] += 1
#                 cnt += 1
#         if cnt > res:
#             res = cnt
#     return res


def main():
    n = input()
    arr = [int(i) for i in input().split()]
    print(get_longest(arr))


main()