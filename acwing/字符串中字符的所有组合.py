"""
输入一个字符串，输出该字符串中字符的所有组合。例如abc，它的组合有a、b、c、ab、ac、bc、abc。
"""


def main(s):
    s = list(s)
    global res, temp, n
    n = len(s)
    res = []
    temp = []

    def dfs(s, idx, u):
        if u == 0:
            res.append(''.join(temp))
            return
        if idx == n:
            return
        # 选当前字符
        temp.append(s[idx])
        dfs(s, idx + 1, u - 1)
        temp.pop()
        # 不选当前字符
        dfs(s, idx + 1, u)

    for u in range(1, len(s)+1):
        dfs(s, 0, u)
    print(res)


s = 'abc'
main(s)
