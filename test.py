"""
input="abc"
a
b
c
ab
ac
bc
abc
""
"""


def main(s):
    res, temp = [], []
    mark = [0] * len(s)

    def dfs(t):
        if ''.join(sorted(temp)) not in res and len(temp):
            res.append(''.join(temp))
        if t == len(s):
            return
        for i in range(t, len(s)):
            if not mark[i]:
                temp.append(s[i])
                mark[i] = 1
                dfs(t+1)
                mark[i] = 0
                temp.pop()
    dfs(0)
    return res


input = "abc"
print(main(input))
