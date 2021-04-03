# https://atcoder.jp/contests/panasonic2020/tasks/panasonic2020_b

H,W = map(int, input().split())
field = H * W
if H == 1 or W == 1:
    print(int(1))
    exit()

if field % 2 == 0:
    res = field / 2
else:
    res = (field // 2) + 1

print(int(res))
