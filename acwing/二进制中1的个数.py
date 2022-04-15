""" 题解
二进制技巧：
1）求n的第k位数字 n>>k&1
2）清除n最低位的1 lowbit(n)=n&(n-1)

5   &  4  
101 &  100 =》100
6   &  5
110 &  101 =》100
4   &  3
100 &  011 =》000
故n & n-1会消除最低位的1

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


def get_lowbit(n):
    return n & -n


def main():
    _ = int(input())
    arr = list(map(int, input().split()))
    res = []
    for i in range(len(arr)):
        t = arr[i]
        cnt = 0
        while t:
            cnt += 1
            t -= get_lowbit(t)
        res.append(cnt)
    print(' '.join([str(i) for i in res]))


main()
