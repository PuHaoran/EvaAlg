"""
维持一个单调递增的栈，如果栈顶元素大于等于当前元素则出栈，直至找到小于当前元素的元素，然后将该元素进栈。

5
3 4 2 7 5
输出样例：
-1 3 -1 2 2
"""


def main():
    top, s = -1, [0] * 100010
    _ = input()
    res = []
    arr = list(map(int, input().split()))
    for i in range(len(arr)):
        while top != -1 and arr[i] <= s[top]:
            top -= 1
        if top == -1:
            m = -1
        else:
            m = s[top]
        res.append(m)
        top += 1
        s[top] = arr[i]
    for i in range(len(res)):
        print(res[i], end=' ')


main()
