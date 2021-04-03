# https://atcoder.jp/contests/abc086/tasks/abc086_b
a, b = map(str, input().split())
res = int(a + b)
n = 0

while n < res:
    if n * n == res:
        ans = "Yes"
        break
    n += 1
    ans = "No"

print(ans)
