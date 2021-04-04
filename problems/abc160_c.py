# https://atcoder.jp/contests/abc160/tasks/abc160_c
K,N = map(int,input().split())
A = list(map(int, input().split()))
subs = []
for i in range(N-1):
    sub = A[i+1] - A[i]
    if sub < 0:
        sub *= -1
    subs.append(sub)

last_distance = (K - A[N-1]) + A[0]
if last_distance < 0:
    last_distance *= -1
if last_distance != 0:
    subs.append(last_distance)

ans = sum(subs) - max(subs)
print(ans)
