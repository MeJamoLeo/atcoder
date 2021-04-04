# https://atcoder.jp/contests/abc161/tasks/abc161_c

import random
N = random.randint(0,10**2)
K = random.randint(1,10**2)
count = 1
print(N,K)

# N, K = map(int, input().split())

if K == 1:
    print(0)
    exit()

sub = max(N,K) - min(N,K)
while N > sub:
    N = sub
    sub = max(N,K) - min(N,K)
    print(str(count)+":",N,K)
    count += 1

print(N)
