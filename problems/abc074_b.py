# https://atcoder.jp/co/abc074/tasks/abc074_b
N = int(input())
K = int(input())
X = list(map(int,input().split()))
ans = 0

for i in range(N):
    ans += min(X[i], K-X[i])

print(ans * 2) # x2 for return distance
