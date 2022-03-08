

def main():
    n = int(input())
    arr = [0] * 100010
    p, q = -1, -1
    for _ in range(n):
        row = input().split()
        op = row[0]
        if op == 'push':
            q += 1
            arr[q] = int(row[1])
        elif op == 'empty':
            if p == q:
                print("YES")
            else:
                print("NO")
        elif op == 'pop':
            p += 1
        elif op == 'query':
            print(arr[p+1])


main()
