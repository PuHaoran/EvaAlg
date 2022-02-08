"""

"""
""" 题解
二进制技巧：
1）求n的第k位数字 n>>k&1
2）清除n最低位的1 lowbit(n)=n&(n-1)

解法一
5
1 2 3 4 5
1 1 2 1 2
模拟求二进制操作
2 5...1  (1)
2 2...0  (2)
2 1...1  (3)
  0
=> 101
2 11...1  (1)
2 5...1  (2)
2 2...0  (3)
2 1...1  (4)
  0
=> 1101
解法二
不断消除n最低位的1，直到n为0
while n:
    n = n & (n-1)
"""
def get_one_num(n):
    cnt = 0
    while n:
        n = n & (n - 1)
        cnt += 1
    return cnt
# def get_one_num(x):
#     cnt = 0
#     while x:
#         t = x % 2
#         x = x // 2
#         if t:
#             cnt += 1
#     return cnt


def main():
    _ = input()
    arr = [int(i) for i in input().split()]
    res = []
    for i in range(len(arr)):
        res.append(str(get_one_num(arr[i])))
    print(' '.join(res))


main()
