""" 题解
6 3
1 2 2 1 2 1
1 3 1
3 5 1
1 6 1

1 2 2 1 2 1
差分操作=》
1 1 0 -1 1 -1
2 1 0 -2 1 -1   (1 3 1) b[l]+c b[r+1]-c
2 1 1 -2 1 -2   (3 5 1)
3 1 1 -2 1 -2   (1 6 1)

3 4 5 3 4 2
"""


def main():
    n, m = map(int, input().split())
    arr = [0]+list(map(int, input().split()))
    f = [0] * (n+2)

    for i in range(1, len(arr)):
        f[i] = arr[i] - arr[i-1]

    for _ in range(m):
        l, r, c = map(int, input().split())
        f[l] += c
        f[r+1] -= c
    for i in range(1, len(arr)):
        f[i] += f[i-1]
    print(' '.join([str(i) for i in f[1:n+1]]))


main()
