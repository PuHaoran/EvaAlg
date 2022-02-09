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
    m, q = map(int, input().split())
    arr = list(map(int, input().split()))
    diff_arr = [arr[i]-arr[i-1] if i != 0 else arr[i] for i in range(len(arr))]
    for i in range(q):
        _ = [int(i) for i in input().split()]
        l, r, c = _[0]-1, _[1]-1, _[2]
        diff_arr[l] += c
        if r+1 < len(diff_arr):
            diff_arr[r+1] -= c
    for i in range(len(diff_arr)):
        if i != 0:
            diff_arr[i] += diff_arr[i-1]
    print(' '.join([str(i) for i in diff_arr]))


main()
