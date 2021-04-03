# https://atcoder.jp/contests/abc068/tasks/abc068_b
N = int(input())
box = []
i = 1

while i <= 200:
    box.append(i)
    i *= 2

i = 0

for i in range(len(box)):
    if box[i] == N:
        ans = N
        break
    if N < box[i]:
        ans = box[i - 1]
        break

print(ans)
